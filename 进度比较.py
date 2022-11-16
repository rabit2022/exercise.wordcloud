import os

from mybase import step_hms
from init import *

filename = pref + "logging.txt"
columns = ["nowtime", "current_progress"]

data = pd.read_csv(filename, header=None, names=columns, dtype=(float, float))

# https://blog.csdn.net/lildn/article/details/114585316
# 判断有无重复数据
# data = data.duplicated()
# 判断两列'age', 'surname'有无重复数据
# data = data.duplicated(subset=["nowtime", "current_progress"])
# 去掉重复数据
# data = data.drop_duplicates(subset=["nowtime", "current_progress"])
# 去掉重复数据 保留后者
data = data.drop_duplicates(subset=columns, keep='last')

# data = data.apply(step_hms, axis = 1)
# print(data)

x_train = data[columns[0]]
y_train = data[columns[1]]

plt.plot(x_train, y_train, "-r", label="correct")
plt.plot(x_train, y_train, "b.", label="Train data")

plt.xlabel(columns[0])
plt.ylabel(columns[1])

title = "progress curve"
plt.title(title)
plt.legend()  # 需要label

plt.savefig(pref + title, dpi=150)
plt.show()
