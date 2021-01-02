# -*- coding: utf-8 -*-
# @Time    : 2021年01月02日21:53
# @Author  : SoonCj
# @Email   : F_aF_a@163.com
# @File    : LFM.py
# @Software: PyCharm
"""
说明:
用梯度下降法求矩阵的逆
"""
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def inverse(a):
    b = np.zeros_like(a)
    n = len(a)
    c = np.eye(n)
    alpha = 1
    for times in range(200):
        for i in range(n):
            for j in range(n):
                err = c[i][j]
                for k in range(n):
                    b[i][j] += a
    return b.T
