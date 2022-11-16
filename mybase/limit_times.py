import time
import functools

from .error_except import catchUnicodeDecodeError

# https://blog.csdn.net/weixin_39765100/article/details/110401693?utm_medium=distribute.wap_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-110401693-blog-111917332.wap_relevant_multi_platform_whitelistv1&spm=1001.2101.3001.4242.1&utm_relevant_index=1
def limit_called_times(times=10):
    """限制调用次数"""

    def wrapper(func):

        cache = {}
        if isinstance(times, (int, float)):
            limit_times = [int(times)]
        else:
            limit_times = [10]

        def _called_time(*args, **kwargs):
            key = func.__name__
            if key in cache.keys():  # 函数存在
                [call_times, updatetime] = cache[key]
                # call_times调用次数
                # updatetime调用时间
                if time.time() - updatetime < 60:
                    # 60秒内，调用次数加1
                    cache[key][0] += 1
                else:  # 60秒外，次数重置
                    cache[key] = [1, time.time()]
            else:  # 不存在时新建
                call_times = 1
                cache[key] = [call_times, time.time()]
                # print('调用次数: %s' % cache[key][0])
                print("限制次数: %s" % limit_times[0])

            if cache[key][0] <= limit_times[0]:
                # 调用<限制，执行函数，记录时间
                res = func(*args, **kwargs)
                cache[key][1] = time.time()
                return res
            else:
                print("超过调用次数了")
                return None

        return _called_time

    return wrapper


@catchUnicodeDecodeError
def completion_progress(total_line, code_model):
    """
    显示完成进度, 在循环下的子任务封装成函数，并用此装饰器装饰, 只需传入total_line参数
    total_line:int, str
        总完成进度, 传入str时，认为是文件路径，计算文件的总行数，作为总进度
    code_model:不能传入, 
        由catchUnicodeDecodeError装饰器完成参数传入, 否则会发生错误
    
    """
    if isinstance(total_line, (int, float)):
        total_line = int(total_line)
    elif isinstance(total_line, str):
        # 认为是文件路径
        total_line = len(open(total_line, "r", encoding=code_model).readlines())

    @functools.lru_cache(maxsize=32)
    def middle(func):
        # 列表内元素可变，不用nonlocal
        count_times = [0]  # 调用次数
        starttime = [time.time()]  # 开始时间
        exe_times = [0]# 执行次数
        

        def wrapper(*args, **kwargs):
            # 执行子任务
            res = func(*args, **kwargs)
            count_times[0] += 1
            nowtime = time.time()
            
            # 已使用时间
            delta = nowtime - starttime[0]
            # 当前进度
            current_progress = count_times[0] / total_line * 100
            # 预测还需要的时间
            needed_time = (100 - current_progress) / (current_progress / delta)

            # 完成一次后的任务
            if not current_progress % 100:
                
                print(
                    "当前进度: %.1f%%  仍需: %.0f秒  花费: %.2f秒"
                    % (current_progress, needed_time, delta)
                )
                
                # 应对连续的执行相同的任务
                starttime[0] = time.time()
                # 进度归0
                count_times[0] = 0
                
                
                exe_times[0] += 1
                if exe_times[0]>1:# 2次以后显示执行次数
                    print("当前执行:{}次".format(exe_times[0]))
                    
            else:
                print(
                    "当前进度: %.1f%%  仍需: %.0f秒  花费: %.2f秒"
                    % (current_progress, needed_time, delta),
                    end="\r",
                )

            return res

        return wrapper

    return middle


if __name__ == "__main__":

    @completion_progress(1000)
    def foo():
        # print("I'm foo")
        for _ in range(100):
            print("aaa")

    for _ in range(1000):
        foo()

    # print(1.6 in {2, 5, 1.6})
