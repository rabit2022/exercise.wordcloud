# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l16平均时间.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


from timeit import Timer

t1 = Timer("seg_book()", "from l06中文的词云 import seg_book")
num = 20
times = t1.timeit(number=num)  # 总共花费时间
print("avrage %f seconds" % (times / num))
