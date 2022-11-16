import time
import functools

from ..error_except import catchUnicodeDecodeError
from .time_trans import step_hms
from  .savelog import save_log



@catchUnicodeDecodeError
def completion_big_progress(total_line, code_model):
    """大型文件, 显示完成进度
    花费时间在1小时左右的计时
    """
    if isinstance(total_line, (int, float)):
        total_line = int(total_line)
    elif isinstance(total_line, str):
        # 认为是文件路径
        total_line = len(open(total_line, "r", encoding=code_model).readlines())
    elif isinstance(total_line, (list, tuple)):
        # 计数
        total_line = len(total_line)

    @functools.lru_cache(maxsize=32)
    def middle(func):
        # 列表内元素可变，不用nonlocal
        count_times = 0  # 调用次数
        start_time = time.time()  # 开始时间

        exe_times = 0  # 执行次数

        def wrapper(*args, **kwargs):
            # 执行子任务
            res = func(*args, **kwargs)

            nonlocal start_time, count_times
            count_times += 1  # 计数加1
            delta = time.time() - start_time  # 已使用时间
            delta = round(delta, 2)
            

            def complete(current_progress):
                """已完成"""
                if current_progress >= 100:  # 非实时显示，条件有所更改
                    delta_s = step_hms(delta)
                    
                    # 完成一次后的任务
                    print("当前进度:100%%  仍需0  花费%s" % (delta_s))

                    nonlocal start_time, count_times
                    # 应对连续的执行相同的任务
                    start_time = time.time()
                    count_times = 0  # 进度归0

                    nonlocal exe_times
                    exe_times += 1
                    if exe_times > 1:  # 大函数执行2次以后, 显示执行次数
                        print("当前执行:第{}次".format(exe_times))
                    return res

            def not_complete():
                if not delta % 6:  # 每6秒计算一次, 减少计算量
                    # 计算部分
                    current_progress = count_times / total_line * 100  # 当前进度，100为完成度
                    current_progress = round(current_progress, 1)

                    complete(current_progress)

                    needed_time = (100 - current_progress) / (
                        current_progress / delta
                    )  # 预测完成时间

                    # 转为字符串
                    needed_time_s = step_hms(needed_time)
                    delta_s = step_hms(delta)

                    print(f"当前进度:{current_progress}%  仍需{needed_time_s}  花费{delta_s}", end="\r")
                    
                    save_log(delta, current_progress)
                    
                    

            not_complete()

            return res

        return wrapper

    return middle
