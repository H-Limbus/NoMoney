#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  checkfile.py

import os


def checkFile(outputPath):
    return outputPath if whetherFileExist(outputPath) else createFilePath(outputPath)


def whetherFileExist(outputPath):
    if os.path.exists(outputPath):
        whetherCover = input('文件已经存在，是否覆盖？（y or n 不覆盖直接退出, 默认不覆盖）：')
        print('\n')
        if whetherCover == 'y':
            open(outputPath, 'w').close()
            return True
        else:
            exit()
    else:
        return False


def createFilePath(outputPath):
    if '/' in outputPath and '\\' in outputPath:
        print('文件路径输入有误！')
        return
    elif '//' or '\\' in outputPath:
        outputPath = outputPath.replace('\\', '/').replace('//', '/').split('/')
    else:
        outputPath = outputPath.split('/')
    if outputPath[0] is '.':
        open('/'.join(outputPath), 'w').close()
    else:
        path = ''
        for i in outputPath[:-1]:
            path += i + '/'
            if os.path.exists(path): continue
            else: os.makedirs(path)
        open('/'.join(outputPath), 'w').close()
    return '/'.join(outputPath)
