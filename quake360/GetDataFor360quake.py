#    -*- coding: 'utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  GetDataFor360quake.py


import requests
from alive_progress import alive_bar
from config.Config import (QUAKE_API, DEFAULT_START_TIME, DEFAULT_END_TIME, ageHalfYearDate, ageOneMonthDate)


def GDF360quake(logger):
	if QUAKE_API == '':
		logger.error("360quake is not fully configured.")
	else:
	    # 360quake user information query
	    url = "https://quake.360.cn/api/v3/search/quake_service"
	    headers = {"X-QuakeToken": QUAKE_API, "Content-Type": "application/json"}
	    restCredit = int(requests.get("https://quake.360.net/api/v3/user/info", headers=headers).json()['data']['month_remaining_credit'])
	    
	    searchSyntax = input('ipnut 360-quake search syntax:  ')
	    print('''
	            select time node (default is within one year)

	                1、one month
	                2、half year

	    ''')
	    s = input('input the time node (default Enter): ')
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
	        logger.info(f'There are {totalCount}t data, rest quota{str(restCredit)}')
	        while 1:
	            getDataCount = input('1 data = 1 quota, how much data you need (q exit): ')
	            print('\n')
	            if getDataCount == 'q': exit()
	            if int(getDataCount) <= 10:
	                with alive_bar(1) as bar:
	                    yield [(i['ip'] + ':' + str(i['port'])) for i in page['data']]
	                    bar()
	                break
	            elif int(getDataCount) <= restCredit:
	                with alive_bar(unknown="stars", title="getting") as bar:
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
	                logger.error(f'the remaining quota month are not enough to query {getDataCount}t data, try again! ')
	            else:
	                logger.error('input error, try again! ')


def RequestsRes(url, headers, data, logger):
    page = requests.post(url, headers=headers, json=data).json()
    if 'Successful' not in page['message']:
        logger.info(page['message'])
        return False
    return page
