# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l03分词处理.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


import jieba


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())  # strip()用来消除前后的空格

    outstr = ""
    for word in sentence_seged:
        if word != "\t":
            outstr += word
            outstr += " "  # 去掉制表符并用空格分隔各词
    return outstr.strip()


if __name__ == "__main__":
    msg = seg_sentence("欢迎来到我的领域")
    print(msg)
