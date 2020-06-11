# -*- coding: utf-8 -*-
# @File : test_order.py
# @Author : lb
# @Date : 2020/6/9
# @SoftWare : PyCharm

# 测试pytest-order插件
# 控制测试用例执行顺序
import pytest


class TestPytestOrder:
    # @pytest.mark.run(order=1)
    def test_one(self):
        print("测试用例1")

    # @pytest.mark.run(order=3)
    def test_three(self):
        print("测试用例3")

    # @pytest.mark.run(order=2)
    def test_two(self):
        print("测试用例2")
