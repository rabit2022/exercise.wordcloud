# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l12完整版.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


# 是生成部分的完整的代码，文本随便找一个文本即可。关于中文文本的处理，可以参考上面第二部分的内容。

import os


import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
from scipy.ndimage import gaussian_gradient_magnitude

from mybase import showtime, get_book_name


input_path = "./resourse/book/2021.05-2022.06.txt"

middle = get_book_name(input_path)
output_path = "./生成文件/{}.txt".format(middle)  # 3.88s
image_path = "./resourse/image/04.png"
font_path = "./resourse/font/小南同学.ttf"
save_path = "./生成文件/{}.png".format(middle)


@showtime
def colourful_picture():
    # 图片的处理
    img = Image.open(image_path)
    mask_color = np.array(img)
    mask_color = mask_color[::3, ::3]
    mask_image = mask_color.copy()

    # 把黑色都转换为白色
    mask_image[mask_image.sum(axis=2) == 0] = 255
    # Edge detection
    edges = np.mean(
        [gaussian_gradient_magnitude(mask_color[:, :, i] / 255.0, 2) for i in range(3)],
        axis=0,
    )
    mask_image[edges > 0.08] = 255

    # 绘制词云
    inputs = open(output_path, "r", encoding="utf-8")
    mytext = inputs.read()

    wordcloud = WordCloud(
        mask=mask_image,
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

    # Create coloring from image
    image_colors = ImageColorGenerator(mask_color)
    wordcloud.recolor(color_func=image_colors)

    # 保存至图片
    wordcloud.to_file(save_path)
    inputs.close()


if __name__ == "__main__":
    colourful_picture()
