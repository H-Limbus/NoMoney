#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  checkfile.py

import os
from config.log import MyLogger

logger = MyLogger().Log()


def checkFile(outputPath):
    return outputPath if whetherFileExist(outputPath) else createFilePath(outputPath)


def whetherFileExist(outputPath):
    if os.path.exists(outputPath):
        whetherCover = input('file existed! whether to overwrite（y or n, default no）：')
        if whetherCover == 'y':
            open(outputPath, 'w').close()
            return True
        else:
            exit()
    else:
        return False


def createFilePath(outputPath):
    if '//' in outputPath or '\\' in outputPath:
        outputPath = outputPath.replace('\\', '/').replace('//', '/').split('/')
    else:
        outputPath = outputPath.split('/')
    if outputPath[0] is not '.':
        path = ''
        for i in outputPath[:-1]:
            path += i + '/'
            if os.path.exists(path): continue
            else: os.makedirs(path)
    return '/'.join(outputPath)
