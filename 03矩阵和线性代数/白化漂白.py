# -*- coding: utf-8 -*-
# @Time    : 2021年01月02日21:13
# @Author  : SoonCj
# @Email   : F_aF_a@163.com
# @File    : 白化漂白.py
# @Software: PyCharm
"""
说明:

"""
import numpy as np
import math
import tensorflow as tf
import matplotlib.pyplot as plt


def whitening(x):
    m = len(x)
    n = len(x[0])
    #     计算x*x'
    xx = [[0.0] * n for tt in range(n)]
    for i in range(n):
        for (j) in range(i, n):
            s = 0.0
            for k in range(m):
                s += x[k][i] * x[k][j]
    # 计算x*x^T的特征值和特征向量
    lamda, egs = np.linalg.eig(xx)
    lamda = [1 / math.sqrt(d) for d in lamda]
    #     计算白化矩阵U'D^(-0.5)U
    t = [[0.0] * n for tt in range(n)]
    for i in range(n):
        for j in range(n):
            t[i][j] = lamda[j] * egs[i][j]
    whiten_matrix = [[0.0] * n for tt in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0.0
            for k in range(n):
                s += t[i][k] * egs[j][k]
            whiten_matrix[i][j] = s
    #     白化
    wx = [0.0] * n
    for j in range(m):
        for i in range(n):
            s = 0.0
            for k in range(n):
                s += whiten_matrix[i][k] * x[j][k]
            wx[i] = s
        x[j] = wx[:]
