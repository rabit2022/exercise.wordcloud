# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l00词频统计.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


import jieba.posseg as psg

# 据词频降序排列
def have_sorted(lst):
    word_frequency = {}
    for word in lst:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    word_sort = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    return word_sort


if __name__ == "__main__":

    input_path = "./resourse/book/科幻小说-[柳文扬] 毒蛇.txt"

    # 1. 打开文件
    with open(input_path, "r", encoding="gbk") as f:
        content = f.read()

    # 2. 分离出名词
    lst_words = []
    for x in psg.cut(content):
        # 保留人名，地名，名词，至少2个字
        if x.flag in ["n", "nr", "ns"] and len(x.word) > 1:
            lst_words.append(x.word)

    # 3.据词频降序排列
    lst_sorted = have_sorted(lst_words)
    print(lst_sorted)
