# -*- coding: utf-8 -*-
# @File : test_fix1.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm
import pytest


def test_01(login):
    print("测试conftest用例1。。。")


def test_02():
    print("测试conftest用例2。。。")


def test_03(login):
    print("测试conftest用例3。。。")


if __name__ == '__main__':
    pytest.main(["-s", "test_fix1.py"])
