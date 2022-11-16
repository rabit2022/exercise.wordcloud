# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l14词云style.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


# stylecloud
# 有7865个词云图标供你选择, 需要使用那个图标只需复制下面的图标名称即可！自带停用词的那种
# https://www.zhihu.com/tardis/sogou/art/422322475
"""
import pandas as pd
import jieba.analyse
from stylecloud import gen_stylecloud

# 读取文件
pd_data = pd.read_excel('鸿星尔克.xlsx')
exist_col = pd_data.dropna()  # 删除空行

# 读取内容
text = exist_col['发帖内容'].tolist()

# 切割分词
wordlist = jieba.cut_for_search(''.join(text))
result = ' '.join(wordlist)

gen_stylecloud(text=result,
                icon_name='fas fa-comment-dots',
                font_path='msyh.ttc',
                background_color='white',
                output_name='666.jpg',
                custom_stopwords=['你', '我', '的', '了', '在', '吧', '相信', '是', '也', '都', '不', '吗', '就', '我们', '还', '大家', '你们', '就是', '以后']
               )
print('绘图成功！')
"""

from stylecloud import gen_stylecloud

input_path = "./生成文件/output.txt"
font_path = "./resourse/font/小南同学.ttf"
save_path = "./生成文件/style.png"


def get_picture(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        mytext = f.read()

    gen_stylecloud(
        text=mytext,
        font_path=font_path,
        background_color="black",
        output_name=save_path,
        # 增加配色方案
        palette="cartocolors.qualitative.Bold_5",
        # 修改形状为桃心
        icon_name="fas fa-heart",
        # 设置梯度方向, 颜色渐变方向
        gradient="vertical",
    )


if __name__ == "__main__":
    get_picture(input_path)


# 详细:
# https://blog.51cto.com/phyger/5182230
# 配色方案
palette = "cartocolors.qualitative.Bold_5"
# ​StyleCloud的配色使用了palette样式。​
# ​详情点击：https://jiffyclub.github.io/palettable/

# 梯度方向，水平，垂直
gradient = "horizontal", "vertical"
# 图标
icon_name = "fas fa-    "

# ​StyleCloud的默认形状为旗帜，同时支持Font Awesome提供的免费形状。​
# ​详情点击：https://fontawesome.dashgame.com/
