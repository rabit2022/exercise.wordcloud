# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l13权重分析.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


"""
import pandas as pd
import jieba.analyse
# 读取文件
pd_data = pd.read_excel('鸿星尔克.xlsx')

# 读取内容
text = pd_data['发帖内容'].tolist()

# 切割分词
wordlist = jieba.lcut_for_search(''.join(text))
result = ' '.join(wordlist)

# 设置停用词
stop_words = ['你', '我', '的', '了', '们']
ciyun_words = ''

for word in result:
    if word not in stop_words:
        ciyun_words += word

# 权重分析
tag = jieba.analyse.extract_tags(sentence=ciyun_words, topK=10, withWeight=True)
print(tag)
"""

import jieba.analyse
import matplotlib
import matplotlib.pyplot as plt

input_path = "./生成文件/爆肝工程师的异世界狂想曲.txt"
font_path = "./resourse/font/小南同学.ttf"


def weight_analyse():
    with open(input_path, "r", encoding="utf-8") as f:
        mytext = f.read()

    # 权重分析
    tag = jieba.analyse.extract_tags(sentence=mytext, topK=10, withWeight=True)
    # topK就是指你想输出多少个词，withWeight指输出的词的词频
    print(tag)
    return tag


[
    ("魔法", 0.1905347901382338),
    ("亚里沙", 0.16613323861981855),
    ("波奇", 0.14020818743677865),
    ("小姐", 0.12631172731437296),
    ("小玉", 0.12499126831348512),
    ("卡丽 娜", 0.09283768539812579),
    ("迷宫", 0.07446250620679949),
    ("蜜雅", 0.07326644899554757),
    ("魔物", 0.0681941563727789),
    ("大人", 0.06016632415462503),
]


def data_trans(tag):
    proportion = 0.05
    labels = []
    percents = []
    for label, percent in tag:
        if percent > proportion:
            labels.append(label)
            percents.append(percent)
        else:
            labels.append("其他")
            per = [percent for label, percent in tag if percent <= proportion]
            percents.append(sum(per))
            break
    return labels, percents


def draw_pie(tag):
    labels, percents = data_trans(tag)

    myfont = matplotlib.font_manager.FontProperties(
        fname=font_path
    )  # fname指定字体文件  选简体显示中文

    # plt.xlabel, plt.ylabel, ax.set_xlabel, ax.set_ylabel, plt.xticks, plt.yticks,plt.title,ax.set_title	fontproperties	FontProperties实例
    # plt.legend, ax.legend	prop	fontdict字典
    # plt.xlabel, plt.ylabel,plt.text, ax.text, ax.set_xticklabels, ax.set_yticklabels	fontdict	fontdict字典

    config = {"fontsize": 12, "color": "k", "font": myfont}
    plt.pie(percents, labels=labels, autopct="%1.1f%%", textprops=config)

    # plt.xticks(my_x_ticks,fontproperties = myfont)
    # plt.yticks(my_y_ticks,fontproperties = myfont)

    # plt.xlabel('儿',fontsize=14,fontproperties = myfont)
    # plt.ylabel('加',fontsize=14,fontproperties =myfont)

    plt.title("爆肝工程师", fontproperties=myfont)
    plt.savefig("./生成文件/爆肝工程师.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    tag = weight_analyse()
    draw_pie(tag)
