from multiprocessing import Process,Queue
import os,time

def write(q):
    print("启动wrtite %d" % (os.getpid()))
    for i in range(5):
        q.put(str(i))
        time.sleep(1)
    print("结束wrtite %d" % (os.getpid()))

def read(q):
    print("启动read %d" % (os.getpid()))
    while True:
        value = q.get(True)
        print("value = " + value)

    print("结束read %d" % (os.getpid()))

if __name__ == "__main__":
    print("父进程开始")

    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    #强制结束进程
    pr.terminate()

    print("父进程结束")
