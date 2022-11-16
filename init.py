# 所有用到的库
import os

import numpy as np
# 随机种子，每次随机结果确定
np.random.seed(42)

# %matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
# 标签尺寸
plt.rcParams["axes.labelsize"] = 14
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
# # 中文字体
# plt.rcParams['font.sans-serif'] = [u'SimHei']
# plt.rcParams['axes.unicode_minus'] = False

import pandas as pd

# 忽略警告
import warnings
warnings.filterwarnings("ignore")

pref = "./生成文件/"
# 生成专门的文件夹存储
if not os.path.exists(pref):
    os.makedirs(pref)
