# -*- coding: utf-8 -*-
# @File : homeWork2.py
# @Author : lb
# @Date : 2020/6/5
# @SoftWare : PyCharm
"""
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=短毛，
- 添加一个新的方法， 会捉老鼠
- 复写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=长毛，
- 添加一个新的方法， 会看家，
- 复写父类的【会叫】的方法，改成【汪汪叫】
创建一个猫猫实例
- 调用捉老鼠的方法
- 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
- 调用【会看家】的方法
- 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
"""


# 创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
class Animal:
    # 类属性
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        # print("父类得构造函数")

    # 类方法
    def run(self):
        print("动物会跑。。。")

    # 类方法
    def call(self):
        print("动物会叫。。。")


# 创建子类【猫】，继承【动物类】，
# - 复写父类的__init__方法，继承父类的属性，
# - 添加一个新的属性，毛发=短毛，
# - 添加一个新的方法， 会捉老鼠
# - 复写父类的‘【会叫】的方法，改成【喵喵叫】
class Cat(Animal):
    # 复写父类的方法，继承父类的属性
    def __init__(self, name, color, age, sex):
        # Animal.__init__(name, color, age, sex)
        super().__init__(name, color, age, sex)
        # print("子类构造函数")

    hair = "短发"

    def catch_mouse(self):
        print("我是猫，我会抓老鼠。。。")

    def call(self):
        print("我是一个猫，我会喵喵喵。。。")


"""
创建子类【狗】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=长毛，
- 添加一个新的方法， 会看家，
- 复写父类的【会叫】的方法，改成【汪汪叫】
"""


class Dog(Animal):
    def __init__(self, name, color, age, sex):
        super().__init__(name, color, age, sex)

    hair = "长发"

    def look_after_house(self):
        print("会看家。。。")

    def call(self):
        print("汪汪汪叫。。。")


"""
创建一个猫猫实例
- 调用捉老鼠的方法
- 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
- 调用【会看家】的方法
- 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
"""
# cat = Animal("a","b","c","d")
cat = Cat("黑猫警长", "black", "2", "female")
cat.catch_mouse()
print(f"我叫{cat.name},我的颜色是{cat.color},我今年{cat.age}岁,我的毛发是{cat.hair},我捉到了老鼠")
# print(f"我叫{cat.name},我的颜色是{cat.color},我今年{cat.age}岁,我的毛发是{cat.hair}", cat.catch_mouse())


"""
创建一个狗狗实例
- 调用【会看家】的方法
- 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
"""
dog = Dog("旺财", "yellow", "5", "male")
dog.look_after_house()
print(f"我叫{dog.name},我的颜色是{dog.color},我今年{dog.age}岁,我的毛发是{dog.hair}")
