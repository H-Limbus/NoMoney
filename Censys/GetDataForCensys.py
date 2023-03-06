#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  GetDataForcensys.py

import os
from censys.search import CensysHosts
from config.Config import (CENSYS_EMAIL, CENSYS_API, CENSYS_SCRECT)
from alive_progress import alive_bar


def GDFCensys():
    if checkAccount():
        # (hikvision) and location.country=`China`
        newCensys = CensysHosts()
        quota = newCensys.quota()
        restQuota = str(quota['allowance'] - quota['used'])
        print(f'您的剩余积分有{restQuota}分。')
        while 1:
            searchSyntax = input('请输入 censys 查询语法：')
            print('\n')
            getDataCount = input(f'查询1条数据1积分，您需要多少条数据，(退出输入q)：')
            print('\n\n')
            if getDataCount == 'q': break
            if int(getDataCount) <= int(restQuota):
                with alive_bar(unknown="stars", title="获取中") as bar:
                    query = newCensys.search(searchSyntax, page=1, per_page=int(getDataCount))
                    for i, k in query.view_all().items():
                        sumData = []
                        for t in k['services']:
                            sumData.append(i + ':' + str(t['port']))
                        yield sumData
                        bar()
                break
            elif int(getDataCount) > int(restQuota):
                print(f'您今日积分不够查询{getDataCount}条数据。请重新输入!')
            elif not getDataCount.isdigit():
                print('输入有误，请重新输入!')
    else:
        print('censys的api已经更改，正在更新！')
        osPopen = os.popen("censys config", "w")
        try:
            osPopen.write(CENSYS_API + "\n" + CENSYS_SCRECT + "\nn\n")
            print('更新完毕！')
        except:
            print('更新失败，censys 的api 不正确，请重新获取！')


def checkAccount():
    try:
        if CensysHosts().account()['login'] == CENSYS_EMAIL:
            return True
        else:
            return False
    except:
        return False
