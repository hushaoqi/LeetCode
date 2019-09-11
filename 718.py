#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def findMaxSubListLen(a, b):
    alen = len(a)
    blen = len(b)

    table = [[0 for _ in range(blen+1)] for _ in range(alen+1)]
    for i in range(1, alen+1):
        for j in range(1, blen+1):
            if a[i-1] == b[j-1]:
                table[i][j] = table[i - 1][j - 1] + 1

    return max(max(array) for array in table)


# ******************************结束写代码******************************


_a_i = 0
_a = [1, 2, 3, 2, 1]
_b = [3, 2, 1, 4, 7]


res = findMaxSubListLen(_a, _b)

print(str(res) + "\n")