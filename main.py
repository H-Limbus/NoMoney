# -*- coding: utf-8 -*-
# @Date    :  2022-12-30 14:58:28
# @Author  :  Limbus
# @file    :  main.py

import os
import time
from parse.settingParse import Parse
from rules.rule import PrintRule
from update.UpdateAPI import UpdAPI
from config.Config import PLATES
from config.logo import PrintLogo
from fofa.GetDataForfofa import GDFfofa
from zoomeye.GetDataForzoomeye import GDFzoomeye
from qianxin.GetDataForqianxin import GDFqianxin
from quake360.GetDataFor360quake import GDF360quake
from Censys.GetDataForCensys import GDFCensys


def run():
    start = time.time()
    PrintLogo()
    args = Parse()
    # print(args)
    ConfirmedSet = [i for i in PLATES if args[i]]
    if args['rules'] or args['UpdateCookie']:
        if args['rules']:
            PrintRule(ConfirmedSet)
        if args['UpdateCookie']:
            UpdAPI(ConfirmedSet)
    else:
        from reports.checkfile import checkFile

        outputPath, outputFileFormat = checkFile(args['output']), args['format']

        for name in ConfirmedSet:
            # if name in ['qianxin', '360quake']:
            #     pass
            # else:
            data = globals()['GDF'+name]()
            from reports import base
            base.BaseSaveData(outputPath, data, outputFileFormat)
    print(time.time() - start)



