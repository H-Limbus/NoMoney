#    -*- coding: utf-8 -*-
#  @Date   :  2022-12-31 15:13:14
# @Author  :  Limbus
#  @file   :  __init__.py


import os
from config.Config import CURRENT_PATH

if os.path.exists(f"{CURRENT_PATH}\\temp"):
	pass
else:
	os.mkdir(f"{CURRENT_PATH}\\temp")