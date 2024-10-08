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

		searchSyntax = input('ipnut 360-quake search syntax: ')
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
			"size": 0,
			"ignore_cache": True,
			"start_time": searchDate,
			"end_time": DEFAULT_END_TIME
		}
		page = RequestsRes(url, headers, data, logger)
		if page:
			totalCount = page['meta']['pagination']['total']
			logger.info(f'There are {totalCount}t data, rest quota {str(restCredit)}')
		getDataCount = input('1 data = 1 quota, how much data you need (q exit): ')
		if getDataCount == 'q': exit()
		if int(getDataCount) > 500:
			logger.error('a maximum of 500 pieces of data can be queried at a time.')
			exit()
		elif int(getDataCount) <= restCredit:
			data['size'] = int(getDataCount)
			page2 = RequestsRes(url, headers, data, logger)
			if page2:
				with alive_bar(unknown="stars", title="getting") as bar:
					yield [i['ip'] + ':' + str(i['port']) for i in page2['data']]
					bar()
			else:
				exit()
		elif int(getDataCount) > restCredit:
			logger.error(f'the remaining quota month are not enough to query {getDataCount}t data, try again! ')
			exit()
		else:
			logger.error('input error, try again! ')
			exit()


def RequestsRes(url, headers, data, logger):
	page = requests.post(url, headers=headers, json=data).json()
	if page['code'] != 0:
		logger.error('code: '+ page['code'] + '\t' + 'message' + page['message'])
		return False
	return page
