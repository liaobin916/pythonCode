# -*- coding: utf-8 -*-
# @File : conftest.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm

import pytest


@pytest.fixture(autouse="true")
def login():
    print("登录名，登录密码。。。。")
