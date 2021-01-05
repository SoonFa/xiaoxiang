# -*- coding: utf-8 -*-
# @Time    : 2021年01月05日17:06
# @Author  : SoonCj
# @Email   : F_aF_a@163.com
# @File    : 1数据生成.py
# @Software: PyCharm
"""
说明:

"""
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
# np.arange(0, 60, 10)->[0,10,20,30,40,50]
# np.arange(0, 60, 10).reshape((-1, 1))->[0,10,20,30,40,50]^T

print(a)
