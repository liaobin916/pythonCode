# -*- coding: utf-8 -*-
# @File : test_assert.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm
import pytest


def f():
    return 3


def test_func():
    # assert f() == 4
    # assert f()
    # assert "a" in "abc"
    # assert "a" not in "hello"
    assert f() != 4


def test_func2():
    a = f()
    assert a % 2 == 0, f"判断a的为偶数，当前a的值为{a}"


def test_func3():
    with pytest.raises(ZeroDivisionError):
        1 / 0
