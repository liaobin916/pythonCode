# -*- coding: utf-8 -*-
# @File : test_run_step.py
# @Author : lb
# @Date : 2020/6/9
# @SoftWare : PyCharm

# pytest运行模式

def setup_module():
    print("\nsetup_module,只执行一次，当有多个测试类的时候使用")


def teardown_module():
    print("\nteardown_module,只执行一次，当有多个测试类的时候使用")


class TestPytest1:
    @classmethod
    def setup_class(cls):
        print("setup_class,只执行一次")

    @classmethod
    def teardown_class(cls):
        print("teardown_class,执行一次")

    def setup_method(self):
        print("setup_mothod每个测试方法都执行一次")

    def teardown_method(self):
        print("teardown_method每个防翻都执行一次")

    def test_one(self):
        print("测试用例1")

    def test_two(self):
        print("测试用例2")


class TestPytest2:
    @classmethod
    def setup_class(cls):
        print("setup_class,只执行一次")

    @classmethod
    def teardown_class(cls):
        print("teardown_class,执行一次")

    def setup_method(self):
        print("setup_mothod每个测试方法都执行一次")

    def teardown_method(self):
        print("teardown_method每个防翻都执行一次")

    def test_three(self):
        print("测试用例3")

    def test_four(self):
        print("测试用例4")
