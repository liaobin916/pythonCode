# -*- coding: utf-8 -*-
# @File : leetcode35.py
# @Author : lb
# @Date : 2020/6/5
# @SoftWare : PyCharm

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素
"""
nums = [1, 2, 4, 5, 3]


# nums.sort()
# print(nums)
# target = 2
# print(nums.index(target))
# sorted(nums)
# print(nums)

def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)
