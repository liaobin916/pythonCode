# -*- coding: utf-8 -*-
# @File : test_fixture_request.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm
import pytest

test_user_data = ["admin", "user"]
test_pwd_data = ["123", "456"]


@pytest.fixture(scope="module")
def input_user(request):
    user = request.param
    print(f"登录用户名：{user}")
    return user


@pytest.fixture(scope="module")
def input_pwd(request):
    pwd = request.param
    print(f"登录用户名：{pwd}")
    return pwd


@pytest.mark.parametrize("input_user", test_user_data, indirect=True)
@pytest.mark.parametrize("input_pwd", test_pwd_data, indirect=True)
def test_login(input_user, input_pwd):
    a = input_user
    b = input_pwd
    print(f"测试用李中login的返回值{a}")
    print(f"测试用李中login的返回值{b}")
    assert a, "失败原因：密码错误"


if __name__ == '__main__':
    pytest.main(["-s", "test_fixture_request2.py"])
