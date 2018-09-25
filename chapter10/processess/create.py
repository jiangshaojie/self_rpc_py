import multiprocessing
import os
import time
def info():
    print("函数内部的")
    print("主进程Id :",os.getppid())
    print("当前进程id :",os.getpid())
    time.sleep(100)
    # p = multiprocessing.Process(target=info, )
    # p.start()
if __name__=='__main__':
    print("moudlename",__name__)
    print("主进程ID :",os.getppid())
    print("当前进程id :",os.getpid())
    p=multiprocessing.Process(target=info,)
    p.start()
