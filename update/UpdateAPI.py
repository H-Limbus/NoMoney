#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    :  2022-12-31 15:13:14
# @Author  :  Limbus
# @file    :  UpdateAPI.py

"""
This program is mainly used to update the cookies of Zoomeye and Fofa. 
Others have their own API, and even searching through the web will 
consume points. It is better to use it directly.
"""


import json
import psutil
import ddddocr
import asyncio
from PIL import Image
from config.Config import *
from pyppeteer import launch
from config.log import MyLogger


logger = MyLogger().Log()


# Configure some parameters for pyppeter startup

async def GetBrowser(name):
    browser = await launch({
        "ignoreHTTPSErrors": True,                                
        "headless": False,                                  # default headless mode
        # "devtools": True,                                 # whether open developer tools,default closed
        'userDataDir': f'{CURRENT_PATH}/{name}/userdata',   # fofa,zoomeye logined information 
        "args": ARGS})   
    page = await browser.newPage()
    await page.setViewport({'width': SCREEN_WIDTH, 'height': SCREEN_HEIGHT})

    # remove web checking
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
    return page


def UpdAPI(ConfirmedSet):

    for i in ConfirmedSet:
        if i in ['censys', 'qianxin', '360quake']:
            logger.info(f' {i} no need update。')
            continue
        else:
            page = asyncio.get_event_loop().run_until_complete(GetBrowser(i))
            asyncio.get_event_loop().run_until_complete(globals()['Upd' + i](page))


# fofa cookies update

async def Updfofa(page):
    await page.goto('https://fofa.info/')
    await asyncio.sleep(2)
    try:
        # judge whether it is login status
        
        await page.click('.logoBtn')

    except:
        with open(f'{CURRENT_PATH}\\fofa\\cookies.json', 'w') as f:
            f.write(json.dumps(await page.cookies()))
        logger.error("Fofa's cookies have not expired!")
        await page.close()
        return True

    # analog login  
    await asyncio.sleep(2)
    await page.waitForSelector('.mod_tab > tbody:nth-child(1)')
    await page.type('#username', FOFA_USER)
    await page.type('#password', FOFA_PASS)
    await page.click('#fofa_service')
    await asyncio.sleep(2)
    getOcr = await page.J('#captcha_image')
    await getOcr.screenshot(path=f'{CURRENT_PATH}/temp/TempFofaOCR.png')
    qr = DecodeOCR(Image.open(f'{CURRENT_PATH}/temp/TempFofaOCR.png'))
    await page.type('.mod_tab > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > input:nth-child(1)', qr)
    await asyncio.sleep(2)
    await page.click('#rememberMe')
    await page.click('.mod_but')
    await asyncio.sleep(2)
    while 1:
        try:
            if 'FOFA网络空间测绘系统' not in await page.title():
                logger.error('OCR identification error, re-identifying！')
                await asyncio.sleep(2)
                await page.type('#password', FOFA_PASS)
                getOcr = await page.J('#captcha_image')
                await getOcr.screenshot(path=f'{CURRENT_PATH}/temp/TempFofaOCR.png')
                await page.type(
                    '.mod_tab > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > input:nth-child(1)',
                    DecodeOCR(Image.open(f'{CURRENT_PATH}/temp/TempFofaOCR.png')))
                await page.click('#rememberMe')
                await page.click('.mod_but')
                continue
            else:
                break
        except Exception as e:
            logger.error(e)
            break
    os.remove(f'{CURRENT_PATH}/temp/TempFofaOCR.png')
    await asyncio.sleep(4)
    with open(f'{CURRENT_PATH}\\fofa\\cookies.json', 'w') as f:
        f.write(json.dumps(await page.cookies()))
    logger.info("Fofa's cookie updated!")


# zoomeye's cookies update

async def Updzoomeye(page):
    await page.goto('https://www.zoomeye.org/')
    await asyncio.sleep(4)
    try:
        # judge whether it is login status

        await page.click('.header-login-btn > a:nth-child(1)')
    except:
        page.on('request', lambda request: asyncio.ensure_future(intercept_request(request)))
        await page.goto('https://www.zoomeye.org/searchResult?q=WIFICAM')
        await asyncio.sleep(2)
        with open(f'{CURRENT_PATH}/zoomeye/cookies.json', 'w') as f:
            f.write(json.dumps(await page.cookies()))
            print("zoomeye's cookie have not expired!")
        return True
    
    # analog login
    await page.waitForSelector('#login_form')
    await page.type('div.form-group:nth-child(4) > input:nth-child(1)', ZOOMEYE_USER)
    await page.type('#inputPassword', ZOOMEYE_PASS)
    ca = await page.J('.captcha')
    await ca.screenshot(path=f'{CURRENT_PATH}/temp/TempZoomeyeOCR.png')
    await asyncio.sleep(2)
    qr = DecodeOCR(Image.open(f'{CURRENT_PATH}/temp/TempZoomeyeOCR.png'))
    await page.type('#id_captcha_1', qr)
    await asyncio.sleep(1)
    await page.click('.btn')
    await asyncio.sleep(1)
    
    # the OCR will be identified four times, and if it fails, enter it manually
    i = 2 
    while 1:
        try:
            item = await page.Jx('/html/body/section/div/div/div[2]/form/div[1]')
            tags = await page.evaluate('item => item.textContent', item[0])
        except:
            break
        await asyncio.sleep(1)
        if tags.strip() == '请输入正确的验证码。' and i >= 0:
            ca = await page.J('.captcha')
            await ca.screenshot(path=f'{CURRENT_PATH}/temp/TempZoomeyeOCR.png')
            await asyncio.sleep(3)
            await page.type('#id_captcha_1', DecodeOCR(Image.open(f'{CURRENT_PATH}/temp/TempZoomeyeOCR.png')))
            await asyncio.sleep(1)
            await page.click('.btn')
            await asyncio.sleep(1)
            i -= 1
            continue
        elif tags.strip() == '请输入正确的验证码。' and i < 0:
            logger.info('OCR identification failed')
            ca = await page.J('.captcha')
            await ca.screenshot(path=f'{CURRENT_PATH}/temp/TempZoomeyeOCR.png')
            Image.open(f'{CURRENT_PATH}/temp/TempZoomeyeOCR.png').show()
            captcha = input('please enter OCR: ')
            await page.type('#id_captcha_1', captcha)
            [proc.kill() for proc in psutil.process_iter() if proc.name() == 'Microsoft.Photos.exe']
            await asyncio.sleep(1)
            await page.click('.btn')
            await asyncio.sleep(2)
            continue
    await asyncio.sleep(2)
    page.on('request', lambda request: asyncio.ensure_future(intercept_request(request)))
    await page.goto('https://www.zoomeye.org/searchResult?q=WIFICAM')
    await asyncio.sleep(2)
    with open(f'{CURRENT_PATH}\\zoomeye\\cookies.json', 'w') as f:
        f.write(json.dumps(await page.cookies()))
    logger.info("zoomeye's cookies update")


# OCR anti-indentified mode
def DecodeOCR(n):
    return ddddocr.DdddOcr().classification(n)


# packet capture of zoomeye
async def intercept_request(request):
    if '/api/search?q=' in request.url:
        open(f'{CURRENT_PATH}/zoomeye/cube.txt', 'w').write(request.headers['cube-authorization'])
