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
        logger.error('The file format you entered is incorrect, auto-saved default format (txt).')
        txtSave(outputPath, data)
    logger.info(f'file saved !  --->> {outputPath}')


def txtSave(outputPath, data):
    fp = open(outputPath, 'a+', encoding='utf-8')
    for i in data:
        for _ in i:
            if "*" in _ or "违规数据" in _:
                continue
            if 'https://' in _ or 'http://' in _:
                _ = _.replace('https://', '').replace('http://', '')
                fp.write(_.strip() + '\n')
            else:
                fp.write(_.strip() + '\n')
    fp.close()


def jsonSave(outputPath, data):
    fp = open(outputPath, 'a+', encoding='utf-8')
    for i in data:
        for _ in i:
            if "*" in _ or "违规数据" in _:
                continue
            if 'https://' in _ or 'http://' in _:
                _ = _.replace('https://', '').replace('http://', '')
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
        for i in data:
            for _ in i:
                if "*" in _ or "违规数据" in _:
                    continue
                if 'https://' in _ or 'http://' in _:
                    _ = _.replace('https://', '').replace('http://', '')
                if ':' in _:
                    the = _.split(':')
                    data_list.append([the[0], the[1]])
                else:
                    data_list.append([_, '80'])
        writer.writerows(data_list)
