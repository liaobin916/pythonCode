# -*- coding: utf-8 -*-
# @File : demo1.py
# @Author : lb
# @Date : 2020/6/5
# @SoftWare : PyCharm


# 定义一个有参函数
def func1(name):
    print(f"hello, my name is {name}")


# 定义个无参函数
def func2():
    print("hello world!")


# 定义一个有返回值的函数
def func3():
    return "hello python"


# 定义一个无返回值的函数
def func4():
    print("我的默认返回值是None,请用print输出看看")


# 1、函数内修改全局变量，使用关键字global
# 定义一个全局变量
var = "hello world"


# 定义一个函数，并修改全局变量
def func():
    global var
    var = "hello python"


func()
print(f"看看var的值：{var}")

# 2、import 和 from 模块名 import * 的区别
# import
"""
from A import B在导入过程中 
创建模块对象 将模块对象的引用保存在本地作用域, 
也就是说当前作用域有一个名字叫B的对象,locals()可以查看;
import A 在导入模块的过程 创建模块对象 将模块对象的引用保存在本地
"""

if __name__ == '__main__':
    func1("廖彬")
    func2()
    print(func3())
    # func4()
    print(func4())
