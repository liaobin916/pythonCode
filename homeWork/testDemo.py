# -*- coding: utf-8 -*-
# @File : testDemo.py
# @Author : lb
# @Date : 2020/6/4
# @SoftWare : PyCharm

# a = 5
# def func():
#     global a
#     a = 4
# print(a)
# func()
# print(a)
# print(f"func {a}")
from testDir import country

print(country.__var1)
print(id(country.var))
country.var = "liaobin"
print(country.var)
print(id(country.var))
country.sayHi()
print(locals())
# from country import *
# print(id(var))
# var = "java"
#
# print(id(var))
# sayHi()
# print(locals())
