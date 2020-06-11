# -*- coding: utf-8 -*-
# @File : test_fixture_request.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm
import pytest

test_login_data = [{"user": "admin", "pwd": "1111"}, {"user": "user", "pwd": "123456"}]


@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    pwd = request.param["pwd"]
    print(f"登录用户名：{user}")
    print(f"登录密码：{pwd}")
    if pwd == "123456":
        return True
    else:
        return False


@pytest.mark.parametrize("login", test_login_data, indirect=True)
def test_login(login):
    a = login
    print(f"测试用李中login的返回值{a}")
    assert a, "失败原因：密码错误"


if __name__ == '__main__':
    pytest.main(["-s", "test_fixture_request3.py"])
