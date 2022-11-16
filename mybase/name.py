# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : name.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


import os


def get_book_name(input_path):
    """绝对路径中取名"""
    # os.path.split(path) # 对路径进行分割，以列表形式返回
    # os.path.splitext(path)  # 从路径中分割文件的扩展名

    # 文件名
    middle = os.path.split(input_path)[-1]
    # 去后缀
    middle = os.path.splitext(middle)[0]
    # 对书名处理
    middle = middle.strip("《」 ")
    middle = middle.split("【")[0]
    middle = middle.split("》")[0]
    # 爆肝工程师的异世界狂想曲
    print(middle)
    return middle
