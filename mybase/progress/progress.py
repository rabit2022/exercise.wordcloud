# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : progress.py
# @Time    : 2022-09-27 16:17:37
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


import time
import functools

from ..error_except import catchUnicodeDecodeError
from .time_trans import step_hms
from  .savelog import save_log

@catchUnicodeDecodeError
def completion_progress(total_line, code_model):
    """显示完成进度

    在循环下的子任务封装成函数，并用此装饰器装饰, 只需传入total_line参数

    参数
    ----------
    total_line : int, str文件路径, list
        总完成进度, 传入str时，认为是文件路径，计算文件的总行数，作为总进度
    code_model : 不传值
        由catchUnicodeDecodeError装饰器完成参数传入, 否则会发生错误

    返回值
    ----------
    result :


    参看
    ----------
    catchUnicodeDecodeError:

    示例
    ----------
    >>> completion_progress(100)
    >>> completion_progress()
    >>> completion_progress(["one", "two"])

    """
    if isinstance(total_line, (int, float)):
        total_line = int(total_line)
    elif isinstance(total_line, str):
        # 认为是文件路径
        total_line = len(open(total_line, "r", encoding=code_model).readlines())
    elif isinstance(total_line, (list, tuple)):
        total_line = len(total_line)

    @functools.lru_cache(maxsize=32)
    def middle(func):
        # 列表内元素可变，不用nonlocal
        count_times = [0]  # 调用次数
        start_time = time.time()  # 开始时间
        exe_times = 0  # 执行次数

        def wrapper(*args, **kwargs):
            # 执行子任务
            res = func(*args, **kwargs)

            count_times[0] += 1
            nowtime = time.time()

            nonlocal start_time
            # 已使用时间
            delta = nowtime - start_time
            # 当前进度
            current_progress = count_times[0] / total_line * 100
            # 预测还需要的时间
            needed_time = (100 - current_progress) / (current_progress / delta)

            # 完成一次后的任务
            if not current_progress % 100:

                print(
                    "当前进度:%.1f%%  仍需:%.0f秒  花费:%.1f秒"
                    % (current_progress, needed_time, delta)
                )

                # 应对连续的执行相同的任务
                start_time = time.time()
                # 进度归0
                count_times[0] = 0

                nonlocal exe_times
                exe_times += 1
                if exe_times > 1:  # 大函数执行2次以后, 显示执行次数
                    print("当前执行:{}次".format(exe_times))

            else:
                print(
                    "当前进度:%.1f%%  仍需:%.0f秒  花费:%.1f秒"
                    % (current_progress, needed_time, delta),
                    end="\r",
                )

            return res

        return wrapper

    return middle




if __name__ == "__main__":

    @completion_big_progress(1000)
    def foo():
        # print("I'm foo")
        for _ in range(100):
            print("aaa")

    for _ in range(1000):
        foo()

    # print(1.6 in {2, 5, 1.6})
