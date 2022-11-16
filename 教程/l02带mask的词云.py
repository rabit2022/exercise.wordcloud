# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l02带mask的词云.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


from wordcloud import WordCloud
from PIL import Image
import numpy as np

file_path = "./resourse/book/1.novel"

with open(file_path, "r", encoding="utf-8") as f:  # encoding='GB2312'
    text = f.read()

# 导入字体文件
font_path = "./resourse/font/小南同学.ttf"


image_path = "./resourse/image/01.png"
# 生成带有mask的图片
mask = np.array(Image.open(image_path))

wordcloud = WordCloud(
    font_path=font_path, mask=mask, margin=1, random_state=1, background_color="white"
).generate(text)

wordcloud.to_file("./生成文件/wordcloud_mask.jpg")
