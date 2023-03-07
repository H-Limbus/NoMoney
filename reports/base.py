#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  base.py

import json
import csv


def BaseSaveData(outputPath, data, outputFileFormat, logger):
    if outputFileFormat in ['txt', 'json', 'csv']:
        globals()[outputFileFormat+'Save'](outputPath, data)
    else:
        logger.info('你输入的格式有误，已自动保存为默认格式（txt）。')
        txtSave(outputPath, data)
    logger.info(f'文件已保存，路径为 --->> {outputPath}')


def txtSave(outputPath, data):
    fp = open(outputPath, 'a+')
    for _ in data:
        for i in _:
            fp.write(i.strip() + '\n')


def jsonSave(outputPath, data):
    fp = open(outputPath, 'a+')
    for i in data:
        for _ in i:
            if 'https://' in i or 'http://' in i:
                i = i.replace('https://', '').replace('http://', '')
            if ':' in _:
                the = _.split(':')
                fp.write(json.dumps({'ip': the[0], 'port': the[1]}) + ',\n')
            else:
                fp.write(json.dumps({'ip': _, 'port': '80'}) + ',\n')
    fp.close()


def csvSave(outputPath, data):
    header_list = ["ip", "port"]
    data_list = []
    with open(outputPath, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header_list)
        for _ in data:
            for i in _:
                if 'https://' in i or 'http://' in i:
                    i = i.replace('https://', '').replace('http://', '')
                if ':' in i:
                    the = i.split(':')
                    data_list.append([the[0], the[1]])
                else:
                    data_list.append([i, '80'])
        writer.writerows(data_list)
