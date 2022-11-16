# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l05筛选词性.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


import jieba.posseg as psg


stop_path = "./resourse/table/mystop.txt"

# 创建停用词list
def stopwordslist(filepath):
    # github 上搜索「停用词」
    stopwords = [
        line.strip() for line in open(filepath, "r", encoding="utf-8").readlines()
    ]
    return stopwords


def seg_sentence(sentence):
    # print(sentence)
    # if sentence:
    sentence_seged = psg.cut(sentence.strip())
    stopwords = stopwordslist(stop_path)  # 这里加载停用词的路径
    outstr = ""
    for word, flag in sentence_seged:

        # 保留名词, 人名，地名，至少2个字
        if flag in ["n", "nr", "ns"] and len(word) > 1:
            # 判断是不是停用词
            if word not in stopwords:
                if word != "\t":  # 每行的间隔
                    outstr += word
                    outstr += " "
    return outstr


if __name__ == "__main__":
    input_path = "./resourse/book/科幻小说-[柳文扬] 毒蛇.txt"
    with open(input_path, "r", encoding="gbk") as f:
        content = f.read()

    a = seg_sentence(content)
    print(a)
