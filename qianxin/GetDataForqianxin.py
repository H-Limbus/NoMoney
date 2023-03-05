#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  GetDataForqianxin.py

import time
import requests
from config.Config import (QIANXIN_API_KEY, DEFAULT_START_TIME, DEFAULT_END_TIME, ageHalfYearDate, ageOneMonthDate)
import base64
from math import ceil
from alive_progress import alive_bar


def GDFqianxin():
    session = requests.Session()
    searchDate = ''
    searchSyntax = base64.urlsafe_b64encode(input('请输入qianxin 查询语法：').encode("utf-8")).decode('utf-8')
    print('''
        按照序号选择查询数据的时间节点（默认一年以内）
        1、一个月以内
        2、半年以内
    ''')
    s = input('请输入选择的序号（要是选择默认，直接回车）：')
    if s == '1': searchDate = ageOneMonthDate
    elif s == '2': searchDate = ageHalfYearDate
    else: searchDate = DEFAULT_START_TIME
    url = 'https://hunter.qianxin.com/openApi/search?api-key={}&search={}&page={}&page_size' \
          '=10&is_web=3&start_time={}&end_time={}'
    link = url.format(QIANXIN_API_KEY, searchSyntax, 1, searchDate, DEFAULT_END_TIME)
    page = session.get(link).json()
    if page['code'] != 200: print(page['message'])
    else:
        totalCount = page['data']['total']
        restQuota = page['data']['rest_quota'].replace('今日剩余积分：', '')
        print(f'您查询的语法共有{totalCount}条，今日剩余积分有{restQuota}分。\n')
        while 1:
            getDataCount = input(f'查询1条数据1积分，获得全部资源需要{totalCount}分，您需要多少条数据，(退出输入q)：')
            print('\n\n')
            if getDataCount == 'q': break
            if int(getDataCount) <= 10:
                data = page['data']['arr']
                sumData = []
                for i in data:
                    sumData.append(i['ip'] + ':' + str(i['port']))
                yield sumData
                print('今日剩余积分： ' + page['data']['rest_quota'])
                break
            elif int(getDataCount) <= int(restQuota):
                data = page['data']['arr']
                sumData = []
                for i in data:
                    sumData.append(i['ip'] + ':' + str(i['port']))
                yield sumData
                queryLinkSum = [url.format(QIANXIN_API_KEY, searchSyntax, i, searchDate, DEFAULT_END_TIME) for i in range(2, ceil(int(getDataCount)/10)+1)]
                with alive_bar(len(queryLinkSum), unknown="stars", title="获取中") as bar:
                    for Link in queryLinkSum:
                        sumData = []
                        html = session.get(Link).json()
                        time.sleep(2)
                        try:
                            for i in html['data']['arr']:
                                sumData.append(i['ip'] + ':' + str(i['port']))
                        except:
                            print(html['message'])
                        yield sumData
                        bar()
                break
            elif int(getDataCount) > int(restQuota):
                print(f'您今日积分不够查询{getDataCount}条数据。请重新输入!')
            else:
                print('输入有误，请重新输入!')


