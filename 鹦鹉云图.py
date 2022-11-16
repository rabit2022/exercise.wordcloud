# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l11产生特点颜色和形状的图云.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


# 我们可以看到原始图片中鹦鹉的颜色很好看，我们希望生成的图片的颜色也和原始图像接近。这里我们只需要在上面代码后面加上重新着色即可。下面看一下简单的说明：
# 绘制词云

from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image

from mybase import *

input_path = "./resourse/book/2021.05-2022.06.txt"

middle = get_book_name(input_path)
output_path = "./生成文件/{}.txt".format(middle)  # 3.88s
image_path = "./resourse/image/05.jpeg"
font_path = "./resourse/font/小南同学.ttf"
save_path = "./生成文件/{}.png".format(middle)


@showtime
def get_cloud_pictute():
    # 读取文本
    inputs = open(output_path, "r", encoding="utf-8")
    mytext = inputs.read()

    # 图片的处理
    img = Image.open(image_path)
    mask_color = np.array(img)
    mask_color = mask_color[::3, ::3]
    mask_image = mask_color.copy()

    print("开始生成云图")

    # 生成云图
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
    ).generate(mytext)

    # Create coloring from image
    image_colors = ImageColorGenerator(mask_color)
    print("开始着色")
    wordcloud.recolor(color_func=image_colors)

    # 保存至图片
    wordcloud.to_file(save_path)
    inputs.close()


# 可以看到在 generate 之后，有一个步骤是重新着色。最终的生成的图像如下所示，此时生成图片的颜色和原始图片的颜色也是想接近的。

if __name__ == "__main__":
    get_cloud_pictute()
