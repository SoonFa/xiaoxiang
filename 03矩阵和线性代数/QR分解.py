# -*- coding: utf-8 -*-
# @Time    : 2021年01月02日21:46
# @Author  : SoonCj
# @Email   : F_aF_a@163.com
# @File    : QR分解.py
# @Software: PyCharm
"""
说明:

"""
import numpy as np
import math


def is_shame(a, b):
    n = len(a)
    for i in range(n):
        if math.fabs(a[i] - b[i]) > 1e-6:
            return False
    return True


if __name__ == '__main__':
    a = np.array([0.65, 0.28, 0.07, 0.15, 0.67, 0.18, 0.12, 0.36, 0.52])
    n = math.sqrt(len(a))
    # n=int(n)
    a = a.reshape((n, n))
    value, v = np.linalg.eig(a)

    times = 0
    while (times == 0) or (not is_shame(np.diag(a), v)):
        v = np.diag(a)
        q, r = np.linalg.qr(a)
        a = np.dot(r, q)
        times += 1
        print("正交阵:\n", q)
        print("三角阵:\n", r)
        print("近似阵:\n", a)
    print("次数：", times, "近似值:", np.diag(a))
    print("精准特征值:", value)
