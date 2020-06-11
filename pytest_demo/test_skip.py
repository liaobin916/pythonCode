# -*- coding: utf-8 -*-
# @File : test_skip.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm
import pytest


def test_01():
    print("\ncase 01")


@pytest.mark.skip(reason="跳过当前用例")
def test_02():
    print("case 02")


def test_03():
    print("case 03")


if __name__ == '__main__':
    pytest.main(["-s", "test_skip.py"])
