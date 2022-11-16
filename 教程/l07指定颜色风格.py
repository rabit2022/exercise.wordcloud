# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l07指定颜色风格.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


# colormap 起作用，需要设置 mode='RGBA'。

wordcloud = WordCloud(
    mask=mask,
    width=800,
    height=800,
    background_color="white",
    margin=1,
    max_words=10000,
    min_font_size=10,
    max_font_size=None,
    repeat=True,
    collocations=False,
    mode="RGBA",
    colormap="Reds",
    font_path="./FZKaTong-M19S.ttf",
).generate(mytext)

# 关键词显示重复
collocations = False
