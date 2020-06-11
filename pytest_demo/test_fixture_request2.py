# -*- coding: utf-8 -*-
# @File : test_fixture_request.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm
import pytest

test_login_data = ["admin", "12345"]


@pytest.fixture(scope="module")
def login(request):
    user = request.param
    print(f"登录用户名：{user}")
    return user


@pytest.mark.parametrize("login", test_login_data, indirect=True)
def test_login(login):
    a = login
    print(f"测试用李中login的返回值{a}")
    assert a != ""


if __name__ == '__main__':
    pytest.main(["-s", "test_fixture_request2.py"])
