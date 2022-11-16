# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : showtime.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


import time


def showtime(func):
    """
    显示时间
    :param func:
    :return:
    """

    def inner_func(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        ending = time.time()
        time_cost = ending - begin
        print("完成此项任务花费了%.2f秒" % (time_cost))
        # print('it cost %f seconds'%(time_cost))
        return result

    return inner_func


def timmer(func):
    def deco(*args, **kwargs):
        print(
            "\n函数：\033[32;1m{_funcname_}()\033[0m 开始运行：".format(
                _funcname_=func.__name__
            )
        )
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(
            "函数: \033[32;1m{_funcname_}()\033[0m 运行了 {_time_}秒".format(
                _funcname_=func.__name__, _time_=(end_time - start_time)
            )
        )
        return res

    return deco
