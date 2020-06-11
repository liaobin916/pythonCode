# -*- coding: utf-8 -*-
# @File : test_mark.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm
import pytest


@pytest.mark.add
def test_mark01():
    print("执行mark01用例。。。")


@pytest.mark.add
def test_mark02():
    print("执行mark02用例。。。")


def test_mark03():
    print("执行mark03用例。。。")


def test_mark04():
    print("执行mark04用例。。。")
