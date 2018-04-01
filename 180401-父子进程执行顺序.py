from multiprocessing import Process
import time
import os

def run(str):
    print("aa ---%s--%s"% (os.getpid(),os.getppid()))
    time.sleep(3)
    print("子进程结束")

if __name__  == "__main__":

    print("主进程启动 -- %s-- %s" % (os.getpid(),os.getppid()))
    #创建进程
    #target 说明子进程的任务
    p = Process(target=run,args=("aa",))
    p.start()

    #等待子进程
    p.join()
    print("主进程结束")