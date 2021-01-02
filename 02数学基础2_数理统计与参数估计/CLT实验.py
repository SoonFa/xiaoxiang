# -*- coding: utf-8 -*-
# @Time    : 2021年01月02日17:25
# @Author  : SoonCj
# @Email   : F_aF_a@163.com
# @File    : CLT实验.py
# @Software: PyCharm
"""
说明:
验证中心极限定理
"""
import numpy
import matplotlib.pyplot as plt

if __name__ == '__main__':
    u = numpy.random.uniform(0.0, 1.0, 10000)
    plt.hist(u, 80, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.show()

    times = 10000
    for time in range(times):
        u += numpy.random.uniform(0.0, 1.0, 10000)
    print(len(u))
    u /= times
    plt.hist(u, 80, facecolor='r', alpha=0.75)
    plt.grid(True)
    plt.show()
