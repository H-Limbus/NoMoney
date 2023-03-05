#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    :  2023-01-05 00:31:16
# @Author  :  Limbus
# @file    :  rule.py


from prettytable import from_csv
from config.Config import CURRENT_PATH


def PrintRule(ConfirmedSet):
    for i in ConfirmedSet:
        fp = open(f'{CURRENT_PATH}/rules/{i}.csv', 'r')
        print('\n'+'-|'*50+'\n')
        print(f'{i}的搜索语法规则：'.center(10)+'\n')
        print(from_csv(fp))

