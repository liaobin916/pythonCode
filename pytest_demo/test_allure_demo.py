# -*- coding: utf-8 -*-
# @File : test_allure_demo.py
# @Author : lb
# @Date : 2020/6/11
# @SoftWare : PyCharm
import allure
import pytest


@pytest.fixture(scope="session")
def login():
    print("用例先登录")


@allure.step("步骤1：点击xxxxxx。。。")
def dtep_1():
    print("1111")


@allure.step("步骤2：点击ooooooo")
def dtep_2():
    print("2222")


@allure.step("步骤3：点击lllllll")
def dtep_3():
    print("3333")


@allure.feature("这是一个编辑模块")
class TestEdit:

    @allure.story("这是一个增加操作")
    def test_1(self, login):
        dtep_1()
        dtep_2()
        dtep_3()
        print("增加成功")

    @allure.story("这是个修改操作")
    def test_2(self):
        print("修改成功。。。")


if __name__ == '__main__':
    pytest.main(["-s", "test_allure_demo"])
