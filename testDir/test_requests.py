# -*- coding: utf-8 -*-
# @File : test_requests.py
# @Author : lb
# @Date : 2020/6/5
# @SoftWare : PyCharm

import requests

data = {
    "username": "python",
    "password": 12345678
}
res = requests.post("http://211.103.136.242:8064/authorizations/", data=data)
print(res.text, sep="\t")
print(res.headers)
print(res.status_code)
import selenium

a = "hello"
b = "world"
print(f"{a} {b}")
