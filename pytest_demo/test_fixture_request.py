# -*- coding: utf-8 -*-
# @File : test_fixture_request.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm
import pytest

test_login_data = [("admin", "admin"), ("user", "123456")]


def login(user, pwd):
    print(f"登录用户名：{user}")
    print(f"登录密码：{pwd}")
    if pwd == "admin":
        return True
    else:
        return False


@pytest.mark.parametrize("user, pwd", test_login_data)
def test_login(user, pwd):
    result = login(user, pwd)
    assert result == True, "失败原因：密码不正确"


if __name__ == '__main__':
    pytest.main(["-s", "test_fixture_request.py"])
