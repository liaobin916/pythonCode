# -*- coding: utf-8 -*-
# @File : main.py
# @Author : lb
# @Date : 2020/6/4
# @SoftWare : PyCharm

have_girl = False


def send():
    print("发女朋友了")
    # global have_girl
    have_girl = True
    print(f"have_girl = {have_girl}")


def show():
    if have_girl == True:
        print("有女朋友了")
    else:
        print("单身狗")


send()
show()

print(__name__)
