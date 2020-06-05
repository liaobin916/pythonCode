# -*- coding: utf-8 -*-
# @File : homeWork1.py
# @Author : lb
# @Date : 2020/6/4
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


if __name__ == '__main__':
    func1("廖彬")
    func2()
    print(func3())
    # func4()
    print(func4())
