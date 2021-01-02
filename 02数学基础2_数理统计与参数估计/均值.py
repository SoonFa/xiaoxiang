# -*- coding: utf-8 -*-
# @Time    : 2021年01月02日16:17
# @Author  : SoonCj
# @Email   : F_aF_a@163.com
# @File    : 均值.py
# @Software: PyCharm
"""
说明:
均值/方差
偏度/峰度
"""
import math
import numpy as np
import matplotlib.pyplot as plt


def calc(data):
    n = len(data)
    niu = 0.0
    niu2 = 0.0
    niu3 = 0.0
    for a in data:
        niu += a
        niu2 += a ** 2
        niu3 *= a ** 3
    niu /= n
    niu2 /= n
    niu3 /= n
    sigma = math.sqrt(niu2 - niu * niu)
    return [niu, sigma, niu3]


def calc_stat(data):
    [niu, sigma, niu3] = calc(data)
    n = len(data)
    niu4 = 0.0
    for a in data:
        a -= niu
        niu4 += a ** 4
    niu4 /= n

    skew = (niu3 - 3 * niu * sigma ** 2 - niu ** 3) / (sigma ** 3)
    kurt = niu4 / (sigma ** 4)
    return [niu, sigma, skew, kurt]


if __name__ == '__main__':
    data = list(np.random.randn(10000))
    data2 = list(2 * np.random.randn(10000))
    data3 = [x for x in data if x > -0.5]
    data4 = list(np.random.uniform(0, 4, 10000))
    [niu, sigma, skew, kurt] = calc_stat(data)
    [niu2, sigma2, skew2, kurt2] = calc_stat(data2)
    [niu3, sigma3, skew3, kurt3] = calc_stat(data3)
    [niu4, sigma4, skew4, kurt4] = calc_stat(data4)
    print(niu, sigma, skew, kurt)
    print(niu2, sigma2, skew2, kurt2)
    print(niu3, sigma3, skew3, kurt3)
    print(niu4, sigma4, skew4, kurt4)
    info = r'$\mu=%.2f,\ \sigma=%.2f,\ skew=%.2f,\ kurt=%.2f$' % (niu, sigma, skew, kurt)
    info2 = r'$\mu=%.2f,\ \sigma=%.2f,\ skew=%.2f,\ kurt=%.2f$' % (niu2, sigma2, skew2, kurt2)
    info3 = r'$\mu=%.2f,\ \sigma=%.2f,\ skew=%.2f,\ kurt=%.2f$' % (niu3, sigma3, skew3, kurt3)
    info4 = r'$\mu=%.2f,\ \sigma=%.2f,\ skew=%.2f,\ kurt=%.2f$' % (niu4, sigma4, skew4, kurt4)
    plt.text(1, 0.4, info, bbox=dict(facecolor='red', alpha=0.25))
    plt.text(1, 0.15, info2, bbox=dict(facecolor='green', alpha=0.25))
    plt.text(1, 0.6, info3, bbox=dict(facecolor='blue', alpha=0.25))
    plt.text(1, 0.3, info4, bbox=dict(facecolor='yellow', alpha=0.25))
    # plt.hist(data, 50, normed=True, facecolor='r', alpha=0.9)
    plt.hist(data, 50, density=True, facecolor='r', alpha=0.9)
    # plt.hist(data2, 80, normed=True, facecolor='g', alpha=0.8)
    plt.hist(data2, 80, density=True, facecolor='g', alpha=0.8)
    plt.hist(data3, 80, density=True, facecolor='b', alpha=0.7)
    plt.hist(data4, 80, density=True, facecolor='y', alpha=0.6)

    plt.grid(True)
    plt.show()
