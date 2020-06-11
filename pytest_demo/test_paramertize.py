# -*- coding: utf-8 -*-
# @File : test_paramertize.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm
import pytest


# 单个
@pytest.mark.parametrize(("a,b"), [[10, 20], (30, 40), (31, 40), (32, 40)])
def test_param(a, b):
    print(a + b)


@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [4, 5])
def test_param1(x, y):
    print(x + y)


if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_paramertize.py"])
