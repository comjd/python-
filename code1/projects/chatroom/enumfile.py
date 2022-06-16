# -*- coding: utf-8 -*-
# @Time : 2022/5/14 下午12:38
# @Author : tyler
# @File : enumfile.py
# @Project : code1
from enum import Enum


class InfoType(Enum):
    login = '1'
    chat = '2'
    logout = '3'
    login_success = '4'
