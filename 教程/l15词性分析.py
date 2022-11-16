# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @File     : l15词性分析.py
# @Time    : 2022-09-27 16:26:01
# @Author  : 穹的兔兔
# @Version : 3.9.7
# @IDE     : pydroid 3
# @origion :
# @Desc   :


"""
import jieba.analyse as ana
import jieba.posseg as psg

stop_path = "./resourse/table/mystop.txt"
# 去除停用词
ana.set_stop_words(stop_path)

sentence="天涯湖北天涯在线书库书库经济学院大数据专业的同学棒棒哒上学打开关闭！"
# 仅过滤停用词
process = ana.extract_tags(sentence)
print(process)

## 直接使用，接口相同，注意默认过滤词性。
process = ana.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'nr'))
print(process)

# 打印权重
if withWeight is True:
    for tag in tags:
        print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
else:
    print(",".join(tags))
    
## 词 + 词性
sentence_seged = psg.cut(sentence.strip())
for s in sentence_seged:
    print(s)
"""

# 提速40, 对大文件明显
# import jieba_fast as jieba

import jieba_fast.analyse as ana
import jieba_fast


stop_path = "./resourse/table/mystop.txt"
# 去除停用词
ana.set_stop_words(stop_path)

# 增加词汇
add_path = "./resourse/table/add.txt"
for line in open(add_path, "r", encoding="utf-8").readlines():
    jieba_fast.add_word(line.strip())


def seg_sentence(sentence):

    sentence_seged = ana.textrank(
        sentence, topK=20, withWeight=False, allowPOS=("ns", "n", "nr")
    )

    outstr = ""
    for word in sentence_seged:
        if len(word) > 1:  # 词数至少2个
            if word != "\t":  # 每行的间隔
                # \t替换为" "
                # 测试样品: 600行 1万4千  毒蛇
                # 3.366秒
                outstr += word
                outstr += " "
                # 3.388秒
                # outstr += (word + " ")

                # 3.445秒
                # outstr = outstr.join((word, " "))
                # 3.412秒
                # outstr = outstr.join(word).join(" ")
                # h8秒
                # outstr = outstr.join(word + " ")
                # 3.550秒
                outstr += word.join(" ")

    return outstr


if __name__ == "__main__":
    sentence = "天涯湖北天涯在线书库书库经济学院大数据专业的同学棒棒哒上学打开关闭！"
    seg = seg_sentence(sentence)
    print(seg)
