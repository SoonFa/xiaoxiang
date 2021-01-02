# -*- coding: utf-8 -*-
# @Time    : 2021年01月2021/1/2日13:04
# @Author  : SoonCj
# @Email   : F_aF_a@163.com
# @File    : Code2.py
# @Software: PyCharm
"""
说明:

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
    print(len(u))
    plt.hist(u, 80, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.show()
