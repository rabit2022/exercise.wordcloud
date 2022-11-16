# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : error_except.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


# 捕获错误


def catchUnicodeDecodeError(func):
    """
    编码错误，gb2312, gbk, gb18030,
    https://ask.csdn.net/questions/668913?sort=id
    文件出现无法解码的乱码。此时1：去除文件中的乱码 ； 2：以字节方式读入，然后decode时
    传入errors='ignore'忽略解码错误即可。强调一下，一定要先确认编码无误。

    中文解码错误
        要求，函数有code_model参数, 但不赋值，否则会有错误出现
    """
    code_list = ["gb2312", "gb18030", "gbk", "utf-8"]
    complete = [False]  # 是否成功解码
    now_code = ["utf-8"]

    def wrapper(*args, **kwargs):

        while code_list:
            if not complete[0]:
                # 依次解码
                now_code[0] = code_list.pop()
            # print("nowcode:{}".format(now_code[0]))
            try:
                result = func(*args, **kwargs, code_model=now_code[0])
                # 解码成功的提示
                print("complete decode:{}".format(now_code[0]))
                complete[0] = True
                return result
            except UnicodeDecodeError:
                continue
            else:
                break

    return wrapper


if __name__ == "__main__":

    @catchUnicodeDecodeError
    def seg_book(code_model):
        if code_model == "ttt":
            raise UnicodeDecodeError
        else:
            print(code_model)

    seg_book()
