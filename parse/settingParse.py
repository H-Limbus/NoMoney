# -*- coding: utf-8 -*-
# @Date    :  2022-12-29 23:57:06
# @Author  :  Limbus
# @file    :  settingParse.py

import argparse


def Parse():
    parser = argparse.ArgumentParser(
        usage='No Money', description='Because I have no money, I have this script(The APIs of this script are all crawlers)')
    parser.add_argument('-f', '--fofa', help='fofa api', action='store_true')
    parser.add_argument('-z', '--zoomeye', help='zoomeye api', action='store_true')
    parser.add_argument('-c', '--Censys', help='censys api', action='store_true')
    parser.add_argument('-q', '--qianxin', help='yingtu api', action='store_true')
    parser.add_argument('-3', '--360-quake', help='360 api', action='store_true', dest='360quake')
    parser.add_argument('-U', '--UpdateCookie', help='update the cookie', action='store_true')
    parser.add_argument('-r', '--rules', help='the api search rules', action='store_true')
    parser.add_argument('-o', '--output', help='Output file', action='store', default='./results.txt')
    parser.add_argument('--format', action='store', metavar='FORMAT', help="Report format (Available: txt, json, csv), default txt", default='txt')
    par = parser.parse_args()
    return vars(par)
