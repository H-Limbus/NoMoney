# -*- coding: utf-8 -*-
# @Date    :  2023-01-06 17:04:05
# @Author  :  Limbus
# @file    :  config.py

import os
import datetime
from win32api import GetSystemMetrics


date = datetime.datetime.now()


#                                   """can change"""
# =======================================================================================

# fofa 账号密码
FOFA_USER = ''
FOFA_PASS = ''


# zooyeye（钟馗之眼）账号密码
ZOOMEYE_USER = ''
ZOOMEYE_PASS = ''



# qianxin（奇安信）api-key（登录之后就可以获取）
QIANXIN_API_KEY = '9797e6f7f35a76f2e5370fd5ba5ba00f7196726ee37c6e27d9681951845bcdd2'



# 360_quake 的api（登录之后就可以获取）
QUAKE_API = '42a48851-beeb-4f0d-ad8c-b99a0acba25f'


# censys的api（登录之后就可以获取）
CENSYS_EMAIL = '2275908981@qq.com'
CENSYS_API = '76835bbd-bc2f-4318-89a4-8309a403bcad'
CENSYS_SCRECT = 'Vu32iC6T08XCELn76CnkIMwFtzd4DxEp'


# 当前的路径
CURRENT_PATH = os.getcwd()




#                     """Try not to modify"""
#  ========================================================================
# 当前脚本支持的平台
PLATES = ['fofa', 'Censys', 'zoomeye', 'qianxin', '360quake']



# 一年的时间节点
DEFAULT_START_TIME = str(int(date.strftime('%Y')) - 1) + date.strftime('-%m-%d')
# 半年的时间节点
ageHalfYearDate = (str(int(date.year) - 1) + '-' + ((str(date.month + 6) + '-') if date.month >= 4 else ('0' + str(date.month + 6) + '-')) + str(date.day)) if (date.month - 6 <= 0) else (str(date.year) + '-' + '0' + str(date.month - 6) + '-' + (str(date.day) if date.day >= 10 else '0' + str(date.day)))
# 一个月的时间节点
ageOneMonthDate = (str(int(date.strftime('%Y')) - 1) + '-12-' + str(date.day)) if (date.month - 1 <= 0) else (date.strftime('%Y-') + (str(date.month - 1) if date.month >= 10 else '0' + str(date.month - 1)) + '-' + (str(date.day) if date.day >= 10 else '0' + str(date.day)))
# 查询结束时间
DEFAULT_END_TIME = date.strftime('%Y-%m-%d')



# 设置屏幕的长宽
SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)



# pyppeteer 的参数设置，改之前可以先了解一下，以免出现问题
ARGS = [
    '--disable-extensions',                                 #  禁用扩展插件
    '--hide-scrollbars',                                    #  隐藏滚动条
    '--disable-bundled-ppapi-flash',                        #  禁用flash
    '--mute-audio',                                         #  静音模式
    '--no-sandbox',                                         #  启用沙盒，关闭沙盒可能有危害
    '--disable-setuid-sandbox',
    # '--disable-gpu',                                      #  不使用gpu
    # f'--window-size={SCREEN_WIDTH},{SCREEN_HEIGHT}',      #  设置界面
    '--disable-infobars',
    '--disable-blink-features=AutomationControlled',        # 新版谷歌浏览器，绕过检测参数配置
    '--start-maximized'
]





