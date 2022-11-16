import os
pref = "./生成文件/"
# 生成专门的文件夹存储
if not os.path.exists(pref):
    os.makedirs(pref)
filename = pref + "logging.txt"

# 清空日志
# with open(filename, "w", encoding = "utf-8") as f:
    # f.write("")

def save_log(*args):
    """记录日志
    
    参数:
    filename:str
        文件名
    args:str
        其他参数
        nowtime, current_progress
    """
    
    
    content = ",".join([str(_) for _ in args])
    content += "\n"
    with open(filename, "a", encoding = "utf-8") as f:
        f.write(content)
        
if __name__ == "__main__":
    # save_log("25145", "30.5")
    # save_log(2545, 50.5)
    ...
    