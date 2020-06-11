# -*- coding: utf-8 -*-
# @File : test_fix2.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm

import pytest


def test_04(login):
    print("测试conftest用例4。。。")


def test_05():
    print("测试conftest用例5。。。")


def test_06():
    print("测试conftest用例6。。。")


if __name__ == '__main__':
    pytest.main(["-s", "test_fix2.py"])
