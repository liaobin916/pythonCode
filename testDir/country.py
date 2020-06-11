# -*- coding: utf-8 -*-
# @File : country.py
# @Author : lb
# @Date : 2020/6/4
# @SoftWare : PyCharm
# from main import send
# from main import show
# send()
# show()

import pytest
import yaml


class TestData:
    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open("E:\pythonCode\homeWork\str2_yaml.yaml")))
    def test_data(self, a, b):
        print(a + b)
