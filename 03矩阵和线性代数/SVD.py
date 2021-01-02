# -*- coding: utf-8 -*-
# @Time    : 2021年01月02日19:55
# @Author  : SoonCj
# @Email   : F_aF_a@163.com
# @File    : SVD.py
# @Software: PyCharm
"""
说明:
奇异值分解
"""
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def restore(sigma, u, v, k):
    print(k)
    m = len(u)
    n = len(v[0])
    a = np.zeros((m, n))
    for k in range(k + 1):
        for i in range(m):
            a[i] += sigma[k] * u[i][k] * v[k]

    b = a.astype('uint8')
    # Image.fromarray(b).save("svd_" + str(k) + ".png")
