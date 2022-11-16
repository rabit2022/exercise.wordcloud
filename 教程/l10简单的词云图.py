# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l10简单的词云图.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


# 首先我们只利用上面图像的形状，让最终的效果是一只鹦鹉：
from wordcloud import WordCloud
import numpy as np
from PIL import Image

input_path = "./resourse/book/绿野仙踪.txt"
output_path = "./生成文件/output.txt"
image_path = "./resourse/image/05.jpeg"
font_path = "./resourse/font/小南同学.ttf"
save_path = "./生成文件/简单鸟图.png"


# 绘制词云
inputs = open(output_path, "r", encoding="utf-8")
mytext = inputs.read()

mask = np.array(Image.open(image_path))  # 模板图片

wordcloud = WordCloud(
    mask=mask,
    margin=1,
    relative_scaling=0,
    max_words=10000,
    min_font_size=10,
    max_font_size=None,
    repeat=True,
    collocations=False,
    mode="RGB",
    font_path=font_path,
).generate(
    mytext
)  # 生成云图


wordcloud.to_file(save_path)
inputs.close()
