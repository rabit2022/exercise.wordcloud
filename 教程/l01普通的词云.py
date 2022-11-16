# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l01普通的词云.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


# https://blog.csdn.net/weixin_33533797/article/details/113718466

import os

from wordcloud import WordCloud
from PIL import Image
import numpy as np

# cur_dir = os.path.dirname(__file__)
# file_path = os.path.join(cur_dir, 'constitution.txt')
file_path = "./resourse/book/1.novel"

# https://blog.csdn.net/qingyuanluofeng/article/details/46514119?spm=1001.2101.3001.6650.4&utm_medium=distribute.wap_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-46514119-blog-115253262.wap_blog_relevant_default&depth_1-utm_source=distribute.wap_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-46514119-blog-115253262.wap_blog_relevant_default
# string中有诸如某些繁体字，gb2312作为简体中文编码是不能进行解析的，必须使用国标扩展码gbk，gbk支持繁体中文和日文假文
# Read the whole text.
with open(file_path, "r", encoding="utf-8") as f:  # encoding='GB2312'
    text = f.read()

# 导入字体文件
# font_path = os.path.join(cur_dir, 'HYC6GFM.TTF')
font_path = "./resourse/font/小南同学.ttf"

# 生成普通的wordcloud
# 我们可以指定使用的字体, 图像的大小和颜色等.
wordcloud = WordCloud(
    font_path=font_path,
    margin=1,
    random_state=1,
    max_words=300,
    width=1000,
    height=700,
    background_color="white",
).generate(text)


pref = "./生成文件/"
# 生成专门的文件夹存储
if not os.path.exists(pref):
    os.makedirs(pref)

save_path = pref + "wordcloud.jpg"
wordcloud.to_file(save_path)
