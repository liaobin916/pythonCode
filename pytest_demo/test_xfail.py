# -*- coding: utf-8 -*-
# @File : test_xfail.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm
import pytest

login_data = [{"user": "admin", "pwd": ""}]


@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    pwd = request.param["pwd"]
    print(f"正在登录的用户名是:{user},密码是{pwd}")
    if pwd:
        return True
    else:
        return False


@pytest.mark.parametrize("login", login_data, indirect=True)
class TestMark:
    def test_login01(self, login):
        res = login
        print(f"case01:{res}")
        assert res == True

    def test_login02(self, login):
        res = login
        print(f"case02:{res}")
        if not res:
            pytest.xfail("login fail, mark xfail")

    def test_login03(self, login):
        res = login
        print(f"case03:{res}")
        if not res:
            pytest.xfail("login fail, mark xfail")


if __name__ == '__main__':
    pytest.main(["-s", "test_mark.py"])
