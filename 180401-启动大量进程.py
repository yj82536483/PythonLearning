from multiprocessing import Pool
import os
import time
import random

def fun(name):
    print("子进程%d开始 %s" % (name, os.getpid()))
    time.sleep(1)
    print("子进程%d结束 %s" % (name, os.getpid()))
    #print(name)


if __name__ == "__main__":
    print("父进程开始")
    p = Pool()
    for i in range(10):
        p.apply_async(fun,args=(i,))

    #在join之前必须调用close，在close之后不能在继续添加新的进程
    p.close()
    #等待进程池所有进程执行完毕，再执行
    p.join()
    print("父进程结束")