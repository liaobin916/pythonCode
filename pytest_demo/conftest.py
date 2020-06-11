# -*- coding: utf-8 -*-
# @File : conftest.py
# @Author : lb
# @Date : 2020/6/10
# @SoftWare : PyCharm

import pytest


@pytest.fixture()
def login():
    print("打印哈哈哈哈哈哈哈哈---------")


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option:type1 or type2"
    )


@pytest.fixture()
def cmdopt(request):
    return request.config.getoption("--cmdopt")
