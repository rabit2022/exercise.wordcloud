# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l08词云与原图融合.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


# 词云与原图融合, 使用 pillow 来对两张图片进行融合
from PIL import Image

image = Image.open("./resourse/image/03.png")
image = image.convert("RGBA")

background = Image.open("./resourse/image/02.png")
background = background.convert("RGBA")  # 两个图片的格式需要相同,大小相同

# r, g, b, alpha = background.split()   #设置图片2透明度
# alpha = alpha.point(lambda i: i>0 and 1000)

img = Image.blend(background, image, 0.7)
# JPG不支持透明度，所以要么丢弃Alpha,要么保存为.png文件    OSError
img.save("./生成文件/blend.png")
