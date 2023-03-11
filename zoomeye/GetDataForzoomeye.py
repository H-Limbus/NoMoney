#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  GetDataForzoomeye.py

"""
use the crawler to obtain the data of zoomeye, the zoomeye's api mode has
not been completed. I'll finish it soon.
"""

import json
import requests
import urllib.parse
from alive_progress import alive_bar
from config.Config import (CURRENT_PATH)


def GDFzoomeye(logger):

    # get zoomeye's cookies and cube
    try:
        fp = json.loads(open(f'{CURRENT_PATH}/zoomeye/cookies.json', 'r').read())
        cube = open(f'{CURRENT_PATH}/zoomeye/cube.txt', 'r').read()
    except FileNotFoundError:
        logger.error("zoomeye's cookies files not exist, try again after update.")
        exit()
    cookies = '; '.join([item["name"] + "=" + item["value"] for item in fp])
    headers = {
        'Host': 'www.zoomeye.org',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cube-Authorization': cube,
        'Connection': 'keep-alive',
        'Referer': 'https://www.zoomeye.org/searchResult?q=WIFICAM',
        'Cookie': cookies,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    url = 'https://www.zoomeye.org/api/search?q={}&page={}&pageSize=20&t=v4+v6+web'
    SearchSyntax = urllib.parse.quote(input("input zoomeye's search syntax: "))
    print('\n')
    session = requests.Session()
    with alive_bar(20, title="getting", bar="circles") as bar:
        for i in range(1, 21):
            data = []
            page = session.get(url.format(SearchSyntax, str(i)), headers=headers)
            if page.json()["status"] == 401:
                logger.info("zoomeye's cookies lose efficacy, try again after update.")
                break
            else:
                for _ in page.json()['matches']:
                    data.append(_['ip'] +':' + str(_['portinfo']['port']))
            yield data
            bar()





