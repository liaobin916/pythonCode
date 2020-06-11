# -*- coding: utf-8 -*-
# @File : test_sample.py
# @Author : lb
# @Date : 2020/6/9
# @SoftWare : PyCharm
import pytest


def test_answer(cmdopt):
    if cmdopt == 'type1':
        print("first1")
    elif cmdopt == "type2":
        print("first2")
    # assert 0


# def add(x, y):
#     return x + y
#
#
# def test_add():
#     assert add(1, 10) == 11
#     assert add(1, 1) == 2
#     assert add(1, 99) == 100
#
#
# class TestClass:
#     def test_one(self):
#         x = "this"
#         print(f"{x}............")
#         assert "h" in x
#
#     def test_two(self):
#         x = "hello"
#         assert hasattr(x, "hello")


if __name__ == '__main__':
    pytest.main(['test_answer.py'])
