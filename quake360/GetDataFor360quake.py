#    -*- coding: 'utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  GetDataFor360quake.py


from config.Config import (QUAKE_API, DEFAULT_START_TIME, DEFAULT_END_TIME, ageHalfYearDate, ageOneMonthDate)
import requests
from alive_progress import alive_bar


def GDF360quake(logger):
    url = "https://quake.360.cn/api/v3/search/quake_service"
    headers = {"X-QuakeToken": QUAKE_API, "Content-Type": "application/json"}
    restCredit = int(requests.get("https://quake.360.net/api/v3/user/info", headers=headers).json()['data']['month_remaining_credit'])
    searchSyntax = input('请输入360_quake 查询语法：')
    print('''
            按照序号选择查询数据的时间节点（默认一年以内）
                1、一个月以内
                2、半年以内
        \n''')
    s = input('请输入选择的序号（要是选择默认，直接回车）：')
    if s == '1': searchDate = ageOneMonthDate
    elif s == '2': searchDate = ageHalfYearDate
    else: searchDate = DEFAULT_START_TIME
    data = {
        "query": searchSyntax,
        "start": 0,
        "size": 10,
        "ignore_cache": True,
        "start_time": searchDate,
        "end_time": DEFAULT_END_TIME
    }
    page = RequestsRes(url, headers, data)
    if page:
        totalCount = page['meta']['pagination']['total']
        logger.info(f'您查询的语法共有{totalCount}条，您本月剩余积分:{str(restCredit)}')
        while 1:
            getDataCount = input(f'查询1条数据1积分，获得全部需要{totalCount}分，您需要多少条数据，(退出输入q)：')
            print('\n')
            if getDataCount == 'q': exit()
            if int(getDataCount) <= 10:
                with alive_bar(1) as bar:
                    yield [(i['ip'] + ':' + str(i['port'])) for i in page['data']]
                    bar()
                break
            elif int(getDataCount) <= restCredit:
                with alive_bar(unknown="stars", title="获取中") as bar:
                    yield [(i['ip'] + ':' + str(i['port'])) for i in page['data']]
                    sumData = []
                    data['size'] = getDataCount
                    page2 = RequestsRes(url, headers, data, logger)
                    if page2:
                        for i in page['data']:
                            sumData.append(i['ip'] + ':' + str(i['port']))
                            bar()
                    yield sumData
                break
            elif int(getDataCount) > restCredit:
                logger.error(f'您这个月的积分不够查询{getDataCount}条数据。请重新输入!')
            else:
                logger.error('输入有误，请重新输入!')


def RequestsRes(url, headers, data, logger):
    page = requests.post(url, headers=headers, json=data).json()
    if 'Successful' not in page['message']:
        logger.info(page['message'])
        return False
    return page