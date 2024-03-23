#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  GetDataForcensys.py

"""
use the official tool of censys to query information
"""


import os
from censys.search import CensysHosts
from config.Config import (CENSYS_EMAIL, CENSYS_API, CENSYS_SCRECT)
from alive_progress import alive_bar


def GDFCensys(logger):

    # check whether to update api and screct

    if checkAccount(logger):
        newCensys = CensysHosts()
        quota = newCensys.quota()
        restQuota = str(quota['allowance'] - quota['used'])
        logger.info(f'your remaining quota: {restQuota}.')
        while 1:
            searchSyntax = input('input censys search syntax: ')
            getDataCount = input('1 data = 1 quota, how much data do you need(q exit): ')
            print('\n')
            if getDataCount == 'q': break
            if int(getDataCount) <= int(restQuota):
                with alive_bar(unknown="stars", title="getting") as bar:
                    query = newCensys.search(searchSyntax, page=1, per_page=int(getDataCount))
                    for i, k in query.view_all().items():
                        sumData = []
                        for t in k['services']:
                            sumData.append(i + ':' + str(t['port']))
                        yield sumData
                        bar()
                break
            elif int(getDataCount) > int(restQuota):
                logger.info(f'your quota are not enough to query {getDataCount} data. Try again! ')
            elif not getDataCount.isdigit():
                logger.error('input error, Try again! ')
    else:

        # api lose efficay or changed, try setting again
        logger.error("censys's api or screct changed, updating...")
        osPopen = os.popen("censys config", "w")
        try:
            osPopen.write(CENSYS_API + "\n" + CENSYS_SCRECT + "\nn\n")
            logger.info('Updated successful! ')
        except:
            logger.error('Updated failed, api wrong, please reacquire! ')


def checkAccount(logger):
	if CENSYS_EMAIL == "" or CENSYS_API == "" or CENSYS_SCRECT == "":
		logger.error("censys is not fully configured.")
		exit()
	else:
	    return True if CensysHosts().account()['login'] == CENSYS_EMAIL else False
