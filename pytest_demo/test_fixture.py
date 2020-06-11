# -*- coding: utf-8 -*-
# @File : test_fixture.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm
import pytest


@pytest.fixture(scope="class")
def login():
    print("setup操作---输入账号，密码登录：")
    yield
    print("teardown操作--退出。。。。。")


class TestFix():
    def test_one(self, login):
        print("用例1")

    def test_two(self, login):
        print("用例2")

    def test_three(self, login):
        print("用例3")


if __name__ == '__main__':
    pytest.main()
