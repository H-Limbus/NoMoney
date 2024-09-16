#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  GetDataForqianxin.py


"""
qianxin(鹰图平台) use api to get data
"""

import time
import base64
import requests
from alive_progress import alive_bar
from config.Config import *


def GDFqianxin(logger):
    if QIANXIN_API_KEY == '':
        logger.error("qianxin is not fully configured.")
        exit()
    else:
        session = requests.Session()
        searchDate = ''
        searchSyntax = base64.urlsafe_b64encode(input('input qianxin search syntax: ').encode("utf-8")).decode('utf-8')
        print('''
            select time node (default is within one year)

                1、one month
                2、half year

        ''')
        s = input('input the time node (default Enter): ')
        if s == '1': searchDate = ageOneMonthDate
        elif s == '2': searchDate = ageHalfYearDate
        else: searchDate = DEFAULT_START_TIME
        url = 'https://hunter.qianxin.com/openApi/search?api-key={}&search={}&page={}&page_size' \
              '={}&is_web=3&start_time={}&end_time={}'
        link = url.format(QIANXIN_API_KEY, searchSyntax, '1', '1', searchDate, DEFAULT_END_TIME)
        page = session.get(link).json()
        if page['code'] != 200: logger.error(page['message'])
        else:
            totalCount = page['data']['total']
            restQuota = page['data']['rest_quota'].replace('今日剩余积分：', '')
            logger.info(f'There are {totalCount}t data，rest quota: {restQuota}.')
            getDataCount = input('1 data = 1 quota, how much data you need (q exit):')
            if getDataCount == 'q': exit()
            if 0 <= int(getDataCount) <= 10:
                yield [i['ip'] + ':' + str(i['port']) for i in page['data']['arr']]
            elif 10 < int(getDataCount) <= int(restQuota):
                yield [i['ip'] + ':' + str(i['port']) for i in page['data']['arr']]
                queryLinkSum = [url.format(QIANXIN_API_KEY, searchSyntax, i, '10', searchDate, DEFAULT_END_TIME) for i in range(2, (int(getDataCount)//10)+3)]
                with alive_bar(len(queryLinkSum), unknown="stars", title="getting") as bar:
                    for Link in queryLinkSum:
                        html = session.get(Link).json()
                        time.sleep(2)
                        yield [i['ip'] + ':' + str(i['port']) for i in html['data']['arr']]
                        bar()
            elif int(getDataCount) > int(restQuota):
                logger.error(f'the remaining points today are not enough to query {getDataCount}, try again! ')
                exit()
            else:
                logger.error('input error, try again! ')
                exit()