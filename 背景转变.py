# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l09词云与遮罩.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


# 我们需要首先将黑色背景转换为白色(一些其他颜色的变化，可以参考下面的代码)，同时我们我们需要检测出物体的边缘。可以使用下面的代码来进行图像的处理(如果有的时候图片比较小，我们可以使用 pillow 中的 resize 对图像进行放大)：


from PIL import Image
import numpy as np

from scipy.ndimage import gaussian_gradient_magnitude

image_path = "./resourse/image/04.png"
save_path = "./生成文件/白色背景.jpeg"

# 图片的处理
img = Image.open(image_path)

mask_color = np.array(img)
mask_color = mask_color[::3, ::3]

mask_image = mask_color.copy()
mask_image[mask_image.sum(axis=2) == 0] = 255  # 把黑色都转换为白色

# Edge detection
edges = np.mean(
    [gaussian_gradient_magnitude(mask_color[:, :, i] / 255.0, 2) for i in range(3)],
    axis=0,
)

mask_image[edges > 0.08] = 255

im = Image.fromarray(mask_image)
im.save(save_path)
