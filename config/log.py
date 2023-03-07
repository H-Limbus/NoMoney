#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  log.py

import sys
from loguru import logger
from config.Config import CURRENT_PATH


class MyLogger:
    def __init__(self):
        self.logger = logger
        self.logger.remove()
        self.logger.add(sys.stderr, level="INFO", format="<green>[{level}]</green>: <yellow>{time:YYYY-MM-DD HH:mm:ss}</yellow> <green>>>> {message}</green>", filter=self.no_error)
        self.logger.add(sys.stderr, level="ERROR", format="<red>[{level}]</red>: <yellow>{time:YYYY-MM-DD HH:mm:ss}</yellow> <red>>>> {message}</red>")
        self.logger.add(f"{CURRENT_PATH}/logFile/log_error.log", level="ERROR", rotation="5 MB", format="[{level}] | {line} | {time:YYYYMMDD HH:mm:ss} | <cyan>{module}</cyan>.<cyan>{function}</cyan> | {message}")

    def Log(self):
        return self.logger

    def no_error(self, record):
        """if debug is False, then filter error and debug msg"""
        return record['level'].name != 'ERROR' and record['level'].name != 'DEBUG'
