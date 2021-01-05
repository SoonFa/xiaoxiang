# -*- coding: utf-8 -*-
# @Time    : 2021年01月05日15:06
# @Author  : SoonCj
# @Email   : F_aF_a@163.com
# @File    : 凸函数举例.py
# @Software: PyCharm
"""
说明:

"""
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)
    u = np.linspace(0, 4, 1000)
    x, y = np.meshgrid(u, u)
    z = np.log(np.exp(x) + np.exp(y))
    ax.contourf(x, y, z, 20)
    plt.show()
