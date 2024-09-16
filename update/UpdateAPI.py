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

import sys
import ddddocr
import subprocess
from PIL import Image
from config.Config import *
from config.log import MyLogger
from playwright.sync_api import sync_playwright, Playwright


logger = MyLogger().Log()

originSysStdout = sys.stdout
sys.stdout = open(os.devnull, 'w')
Ddddocr = ddddocr.DdddOcr()
sys.stdout = originSysStdout

# Configure some parameters for PlayWright startup


def GetBrowser(playwright, name):
        browser = Playwright(playwright).chromium.launch_persistent_context(
            headless=False,
            args=["--start-maximized", "--disable-blink-features=AutomationControlled"],
            user_data_dir=f"{CURRENT_PATH}\\{name}\\userdata",
            no_viewport=True
        )
        page = browser.pages[0]
        return page, browser


def UpdAPI(ConfirmedSet):
    for i in ConfirmedSet:
        if i in ['qianxin', '360quake']:
            logger.info(f' {i} no need update.')
            continue
        else:
            if i == 'fofa' and (FOFA_USER == '' or FOFA_PASS == ''):
                logger.error(f"{i}'s account or password is not configured! ")
            else:
                 with sync_playwright() as playwright:
                    Updfofa(playwright)


# fofa cookies update
def Updfofa(playwright):

    page, browser = GetBrowser(playwright, "fofa")
    page.goto("https://fofa.info/")
    try:
        page.wait_for_selector(".logoBtn", timeout=2000)
        page.locator(".logoBtn").click()
        page.wait_for_timeout(timeout=1800)
        page.locator("#username").fill(FOFA_USER)
        page.locator("#password").fill(FOFA_PASS)
    except:
        browser.storage_state(path=f"{CURRENT_PATH}\\fofa\\cookies.json")
        logger.error("Fofa's cookies have not expired!")
        page.close()
        return True

    page.locator("#captcha_image").screenshot(path=f"{CURRENT_PATH}\\temp\\TempFofaOCR.png")
    getOcr = Ddddocr.classification(Image.open(f"{CURRENT_PATH}\\temp\\TempFofaOCR.png"))
    page.wait_for_timeout(1800)
    page.locator("input[class='mod_input dl_n']").fill(getOcr)
    page.locator('#rememberMe').click()
    page.locator('#fofa_service').click()
    page.locator('.mod_but').click()
    page.wait_for_timeout(1800)

    # analog login
    while 1:
        try:
            if 'FOFA网络空间测绘系统' not in page.title():
                logger.error('OCR identification error, re-identifying！')
                page.wait_for_timeout(1800)
                page.locator("#password").fill(FOFA_PASS)
                page.locator("#captcha_image").screenshot(path=f"{CURRENT_PATH}\\temp\\TempFofaOCR.png")
                getOcr = Ddddocr.classification(Image.open(f"{CURRENT_PATH}\\temp\\TempFofaOCR.png"))
                page.wait_for_timeout(1800)
                page.locator("input[class='mod_input dl_n']").fill(getOcr)
                page.locator('#rememberMe').click()
                page.locator('.mod_but').click()
                continue
            else:
                break
        except Exception as e:
            logger.error(e)
            break
    os.remove(f'{CURRENT_PATH}\\temp\\TempFofaOCR.png')
    page.wait_for_timeout(1800)
    browser.storage_state(path=f"{CURRENT_PATH}\\fofa\\cookies.json")
    logger.info("Fofa's cookie updated!")
