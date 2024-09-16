#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  GetDataForfofa.py

"""
use crawlers to collect data, and update the cookies.
"""

import json
import base64
from json import JSONDecodeError

import requests
from lxml import etree
from alive_progress import alive_bar
from config.Config import CURRENT_PATH


def GDFfofa(logger):
    try:
        # get the lastest cookies from fofa's cookies files

        with open(f'{CURRENT_PATH}\\fofa\\cookies.json', 'r') as f:
            fp = json.loads(f.read())
    except (FileNotFoundError, JSONDecodeError):
        logger.error("fofa's cookies.json is missing, please try again after get it! ")
        exit()
    cookies = '; '.join((i['name'] + '=' + i['value']) for i in fp['cookies'])
    headers = {
        'Host': 'fofa.info',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': cookies,
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    url = 'https://fofa.info/result?qbase64={}&page={}&page_size=10'
    SearchSyntax = base64.b64encode(input('input fofa search syntax: ').encode()).decode()
    session = requests.Session()
    with alive_bar(6, title="getting", bar="circles") as bar:
        for i in range(1, 7):
            page = session.get(url.format(SearchSyntax, str(i)), headers=headers)
            if page.status_code == 502:
                logger.error("fofa's cookies lose efficacy, please reacquire.")
            else:
                html = etree.HTML(page.text).xpath('//*[contains(@class, "hsxa-host")]/a/@href')
                if len(html) == 0:
                    logger.error("If you don't get any data, please check the query statement or update the cookies.")
                    exit()
                else:
                    yield html
            bar()