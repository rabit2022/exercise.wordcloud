# https://www.cnblogs.com/Jasmine6-Lee/p/16138139.html
from time import strftime, gmtime
from functools import lru_cache

import pandas as pd


@lru_cache(maxsize=32)
def seconds_to_hms(seconds_num):
    """
    输入秒数 转换为 时分秒输出
    param: seconds_num integer 666
    return: hms str 00:00:00
    """
    m, s = divmod(seconds_num, 60)
    h, m = divmod(m, 60)
    hms = "%02d:%02d:%02d" % (h, m, s)
    return hms


# divmod() 函数求出两个整数的商和余数
# divmod(a,b) 函数的作用返回一个包含商和余数的元组(a // b, a % b),

# 方法二：strftime('%H:%M:%S',gmtime(x)）


def hms_df(seconds_num, format="%H:%M:%S"):
    """
    输入秒数 转换为 时分秒输出
    :param seconds_num: int 秒数
    :return: str 时分秒字符串
    """
    df = pd.Series(seconds_num)
    df = df.map(lambda x: strftime(format, gmtime(x)))
    return list(df)[0]


def step_df(seconds_num):
    assert isinstance(seconds_num, (int, float)) and seconds_num >= 0
    if seconds_num <= 60:  # 1分钟以内
        return hms_df(seconds_num, "%S")
    elif seconds_num <= 60 * 60:  # 1小时内
        return hms_df(seconds_num, "%M:%S")
    elif seconds_num >= 60 * 60:  # 1小时以上
        return hms_df(seconds_num, "%H:%M:%S")


@lru_cache(maxsize=32)
def step_hms(seconds_num):
    """
    输入秒数 转换为 时分秒输出
    param: seconds_num integer
    return:  str
    """
    m, s = divmod(seconds_num, 60)
    if not m:  # 1分钟以内
        return "%02d" % s

    h, m = divmod(m, 60)
    if not h:  # 1小时内
        return "%02d:%02d" % (m, s)

    # 1小时以上
    return "%02d:%02d:%02d" % (h, m, s)


"""
from time import *

# map函数
x = 13645
x = map(lambda x:strftime('%H:%M:%S',gmtime(x)), [x])
print(list(x))

# df['时长'].map(lambda x:strftime('%H:%M:%S',gmtime(x)))
import pandas as pd

df = pd.Series([13645])
df = df.map(lambda x:strftime('%H:%M:%S',gmtime(x)))
print(list(df))
"""

"""
time.gmtime([secs])
将以自 epoch 开始的秒数表示的时间转换为 UTC 的 struct_time ，其中 dst 标志始终为零。 如果未提供 secs 或为 None ，则使用 time() 所返回的当前时间。 一秒以内的小数将被忽略。 有关 struct_time 对象的说明请参见上文。 有关此函数的逆操作请参阅 calendar.timegm()。

time.strftime(format[, t])
转换一个元组或 struct_time 表示的由 gmtime() 或 localtime() 返回的时间到由 format 参数指定的字符串。如果未提供 t ，则使用由 localtime() 返回的当前时间。 format 必须是一个字符串。如果 t 中的任何字段超出允许范围，则引发 ValueError 。

0是时间元组中任何位置的合法参数；如果它通常是非法的，则该值被强制改为正确的值。
"""

if __name__ == "__main__":
    now = 30
    res = step_floor(now)
    print(res)
