from  multiprocessing import Process
import time

#每个进程拥有自己的数据段，代码段，堆栈段
num= 0
def fun():
    print("子进程开始")

    #子进程修改全局变量不影响父进程中的全局变量
    #创建子进程做了备份num=0
    global  num
    num += 1
    print("子进程结束--%d" % (num))


if __name__ == "__main__":
    print("父进程开始")

    num += 1
    p = Process(target=fun)
    p.start()

    p.join()
    print("父进程结束--%d" % (num))