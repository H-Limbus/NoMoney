#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    :  2022-12-31 15:13:14
# @Author  :  Limbus
# @file    :  UpdateAPI.py

import asyncio
import json
from PIL import Image
import ddddocr
import psutil
from pyppeteer import launch
from config.Config import *
from config.log import MyLogger


logger = MyLogger().Log()


async def GetBrowser(name):
    browser = await launch({
        "ignoreHTTPSErrors": True,
        "headless": False,
        # "devtools": True,
        'userDataDir': f'{CURRENT_PATH}/{name}/userdata',
        "args": ARGS})
    page = await browser.newPage()
    await page.setViewport({'width': SCREEN_WIDTH, 'height': SCREEN_HEIGHT})
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
    return page


def UpdAPI(ConfirmedSet):

    for i in ConfirmedSet:
        if i in ['censys', 'qianxin', '360quake']:
            logger.info(f' {i} 平台不需要更新。')
            continue
        else:
            page = asyncio.get_event_loop().run_until_complete(GetBrowser(i))
            asyncio.get_event_loop().run_until_complete(globals()['Upd' + i](page))


async def Updfofa(page):
    await page.goto('https://fofa.info/')
    await asyncio.sleep(2)
    try:
        await page.click('.logoBtn')
    except:
        with open(f'{CURRENT_PATH}\\fofa\\cookies.json', 'w') as f:
            f.write(json.dumps(await page.cookies()))
        logger.error(' fofa 的 cookie 还没有过期！')
        await page.close()
        return True
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
                logger.error('验证码识别错误，重新识别！')
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
    logger.info(' fofa 的 cookie 已经更新完成！')


async def Updzoomeye(page):
    await page.goto('https://www.zoomeye.org/')
    await asyncio.sleep(4)
    try:
        await page.click('.header-login-btn > a:nth-child(1)')
    except:
        page.on('request', lambda request: asyncio.ensure_future(intercept_request(request)))
        await page.goto('https://www.zoomeye.org/searchResult?q=WIFICAM')
        await asyncio.sleep(2)
        with open(f'{CURRENT_PATH}/zoomeye/cookies.json', 'w') as f:
            f.write(json.dumps(await page.cookies()))
            print('zoomeye 的cookie 还没有过期！')
        return True
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
            logger.info('验证码识别错误，请手动输入！')
            ca = await page.J('.captcha')
            await ca.screenshot(path=f'{CURRENT_PATH}/temp/TempZoomeyeOCR.png')
            Image.open(f'{CURRENT_PATH}/temp/TempZoomeyeOCR.png').show()
            captcha = input('请输入验证码：')
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
    logger.info(' zoomeye 的 cookie 已经更新完成！')


def DecodeOCR(n):
    return ddddocr.DdddOcr().classification(n)


async def intercept_request(request):
    if '/api/search?q=' in request.url:
        open(f'{CURRENT_PATH}/zoomeye/cube.txt', 'w').write(request.headers['cube-authorization'])
