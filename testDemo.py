# -*- coding: utf-8 -*-
# @File : testDemo.py
# @Author : lb
# @Date : 2020/6/4
# @SoftWare : PyCharm

a = 5
def func():
    global a
    a = 4
    # print(a)
func()
print(a)