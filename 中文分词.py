# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l06中文的词云.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :

import jieba_fast
import jieba_fast.analyse as ana

from mybase import *


input_path = "./resourse/book/爆肝工程师的异世界狂想曲【1～21（第四章】.txt"


stop_path = "./resourse/table/mystop.txt"
add_path = "./resourse/table/add.txt"

middle = get_book_name(input_path)
output_path = "./生成文件/{}.txt".format(middle)  # 3.88s
save_path = "./生成文件/{}.png".format(middle)


def seg_sentence(sentence):
    """每句分词时调用"""
    sentence_seged = ana.textrank(
        sentence, topK=20, withWeight=False, allowPOS=("ns", "n", "nr")
    )

    return " ".join([_ for _ in sentence_seged if len(_) > 1 and _ != "\t"])


@catchUnicodeDecodeError
def seg_book(code_model):
    inputs = open(input_path, "r", encoding=code_model)  # 原始的中文文档
    outputs = open(output_path, "w", encoding="utf-8")  # 分词过后的中文文档

    # 去除停用词
    ana.set_stop_words(stop_path)
    with open(add_path, "r", encoding="utf-8") as f:
        # 增加词汇
        for line in f.readlines():
            jieba_fast.add_word(line.strip())

    for line in inputs:
        select_step(line, outputs)

    outputs.close()
    inputs.close()


@completion_big_progress(input_path)
def select_step(line, outputs):
    if line not in "\n\t ":  # 不为空
        line_seg = seg_sentence(line)  # 对每个句子进行分词
        if line_seg:
            # 将处理过后的文件进行保存
            outputs.write(line_seg + "\n")


if __name__ == "__main__":
    seg_book()
