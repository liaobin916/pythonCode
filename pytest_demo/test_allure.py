# -*- coding: utf-8 -*-
# @File : test_allure_demo.py
# @Author : lb
# @Date : 2020/6/11
# @SoftWare : PyCharm
import allure
import pytest


class TestEdit:
    def test_1(self, login):
        print("增加成功")

    def test_2(self):
        print("修改成功。。。")


if __name__ == '__main__':
    pytest.main(["-s", "test_allure_demo"])
