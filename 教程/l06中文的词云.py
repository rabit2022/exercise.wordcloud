# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l06中文的词云.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


import os

from wordcloud import WordCloud
import numpy as np
from PIL import Image

from l15词性分析 import *
from mybase import *

input_path = "./resourse/book/2021.05-2022.06.txt"

middle = get_book_name(input_path)
output_path = "./生成文件/{}.txt".format(middle)  # 3.88s
image_path = "./resourse/image/01.png"
font_path = "./resourse/font/小南同学.ttf"
save_path = "./生成文件/{}.png".format(middle)


@catchUnicodeDecodeError
def seg_book(code_model):
    # 7000行 63万 222秒 金瓶梅
    # 600行 1万4千 3.445秒 3.366秒 毒蛇
    # 5000行 12万 47秒
    # 200000行 220万 776秒 工程师
    # 3000行 22万 樱子小姐 43秒, 44.5
    inputs = open(input_path, "r", encoding=code_model)  # 原始的中文文档
    outputs = open(output_path, "w", encoding="utf-8")  # 分词过后的中文文档

    for line in inputs:
        data_select(line, outputs)

    outputs.close()
    inputs.close()


@completion_big_progress(input_path)
def data_select(line, outputs):
    if line not in "\n\t ":  # 不为空
        line_seg = seg_sentence(line)  # 对每个句子进行分词
        if line_seg:
            # 将处理过后的文件进行保存
            outputs.write(line_seg + "\n")


@showtime
def word_picture():
    mask = np.array(Image.open(image_path))  # 模板图片

    inputs = open(output_path, "r", encoding="utf-8")
    mytext = inputs.read()

    wordcloud = WordCloud(
        mask=mask,
        width=3000,
        height=3000,
        background_color="white",
        margin=1,
        max_words=300,
        min_font_size=10,
        max_font_size=None,
        repeat=False,
        font_path=font_path,
        collocations=False,
        mode="RGBA",
        colormap="Reds",
    ).generate(
        mytext
    )  # 生成云图

    wordcloud.to_file(save_path)
    inputs.close()


if __name__ == "__main__":
    seg_book()
    # word_picture()
