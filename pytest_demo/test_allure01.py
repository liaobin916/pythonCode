# -*- coding: utf-8 -*-
# @File : test_allure01.py
# @Author : lb
# @Date : 2020/6/11
# @SoftWare : PyCharm
import pytest
import allure


@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    def test_login1(self):
        print("登录成功。。。")

    @allure.story("登录失败")
    def test_login2(self):
        print("登录失败。。。")

    @allure.story("登录详情")
    def test_login3(self):
        with allure.step("点击用户名"):
            print("输入用户名。。。")
        with allure.step("点击密码"):
            print("shu输入密码。。。")
        with allure.step("点击登录"):
            print("点击登录。。。。")
        with allure.step("点击登录后，登录失败"):
            assert "1" == 1
            print("登录失败")


if __name__ == '__main__':
    pytest.main(["-s", "test_allure01.py"])
