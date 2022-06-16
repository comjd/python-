#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/19 下午9:55
# @Author : tyler
# @File : infotype.py
# @Project : code1

import enum


class InfoType(enum.Enum):
    UP = 'PUT'
    DOWN = 'GET'
    LIST = 'LIST'
    EXIT = 'QUIT'
    PACKAGE_END = '#*END*#'
    PACKAGE_START = '#*START*#'
