#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  GetDataForfofa.py


import json
import base64
from config.Config import CURRENT_PATH
from lxml import etree
import requests
from alive_progress import alive_bar


def GDFfofa():
    try:
        with open(f'{CURRENT_PATH}\\fofa\\cookies.json', 'r') as f:
            fp = json.loads(f.read())
    except FileNotFoundError:
        print('fofa cookies文件缺失，请更新后再试。')
        exit()
    cookies = '; '.join([item["name"] + "=" + item["value"] for item in fp])
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
    SearchSyntax = base64.b64encode(input('请输入需要查询的fofa语法：').encode()).decode()
    print('\n\n')
    session = requests.Session()
    with alive_bar(6, title="获取中", bar="circles") as bar:
        for i in range(1, 7):
            page = session.get(url.format(SearchSyntax, str(i)), headers=headers)
            if page.status_code == 502:
                print('fofa cookies过期，请更新后再查询！')
            else:
                # print(page)
                html = etree.HTML(page.text).xpath('//*[contains(@class, "hsxa-host")]/a/@href')
                yield html
            bar()


