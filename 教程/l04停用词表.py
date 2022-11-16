# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l04停用词表.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


import jieba

stop_path = "./resourse/table/mystop.txt"

# 创建停用词list
def stopwordslist(filepath):
    # github 上搜索「停用词」
    stopwords = [
        line.strip() for line in open(filepath, "r", encoding="utf-8").readlines()
    ]
    return stopwords


def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist(stop_path)  # 这里加载停用词的路径
    outstr = ""
    for word in sentence_seged:
        if word not in stopwords:  # 判断如果不是停用词
            if word != "\t":
                outstr += word
                outstr += " "
    return outstr
