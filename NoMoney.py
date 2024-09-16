# -*- coding: utf-8 -*-
# @Date    :  2022-12-30 14:58:28
# @Author  :  Limbus
# @file    :  NoMoney.py

"""
 This is the entry of the program,which determines whether to update 
 the API,or print rules,or obtain data.

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as Published by
 the Free software Foundation; either version 2 of the License, or 
 (at your option) any later version.
"""

from parse.settingParse import Parse
from rules.rule import PrintRule
from update.UpdateAPI import UpdAPI
from config.Config import PLATES
from config.logo import PrintLogo
from fofa.GetDataForfofa import GDFfofa
from qianxin.GetDataForqianxin import GDFqianxin
from quake360.GetDataFor360quake import GDF360quake


def run():

    from config.log import MyLogger

    PrintLogo()  # print program Logo
    args = Parse()
    ConfirmedSet = [i for i in PLATES if args[i]]  # parameters obtained from cleaning
    try:
        if args['rules'] or args['UpdateCookie']:
            if args['rules']:
                PrintRule(ConfirmedSet)            # print search syntax or rules
            if args['UpdateCookie']:
                UpdAPI(ConfirmedSet)               # update cookies for the selected platfrom
            exit()
        from reports.checkfile import checkFile
        from reports import base

        logger = MyLogger().Log()

# check whether the file path exists and create file path

        for name in ConfirmedSet:
            data = globals()['GDF' + name](logger)     # Loop call to get data for xx (GDFxx) function
            outputPath, outputFileFormat = checkFile(args['output']), args['format']
            base.BaseSaveData(outputPath, data, outputFileFormat, logger)  # save data

    # when using ctrl+c to stop halfway
    except KeyboardInterrupt:
        logger = MyLogger().Log()
        logger.error("program stopped unexpectedly.")


if __name__ == '__main__':
    run()
