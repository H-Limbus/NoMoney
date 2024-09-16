# -*- coding: utf-8 -*-
# @Date    :  2023-01-06 17:04:05
# @Author  :  Limbus
# @file    :  config.py

import os
from arrow import now

#                                   """can change"""
# =======================================================================================

# fofa 账号密码 | fofa's username and password
FOFA_USER = ''
FOFA_PASS = ''


# qianxin（奇安信）api-key（登录之后就可以获取）
QIANXIN_API_KEY = ''


# 360_quake 的api（登录之后就可以获取）
QUAKE_API = ''


# 当前的路径  | current_path
CURRENT_PATH = os.getcwd()

# PlayWright 的启动配置  | start settings
browserHeadless = False


#                     """Try not to modify"""
#  ========================================================================
# 当前脚本支持的平台
PLATES = ['fofa', 'qianxin', '360quake']


# 一年的时间节点  |  one years ago
DEFAULT_START_TIME = now().shift(years=-1).format("YYYY-MM-DD")
# 半年的时间节点  |  half years ago
ageHalfYearDate = now().shift(months=-6).format("YYYY-MM-DD")
# 一个月的时间节点  |  one months ago
ageOneMonthDate = now().shift(months=-1).format("YYYY-MM-DD")
# 查询结束时间  |   current time
DEFAULT_END_TIME = now().format("YYYY-MM-DD")