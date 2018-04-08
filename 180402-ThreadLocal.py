import threading

num = 1
#让线程有独有的存储空间
local = threading.local()
def run(x,n):
    x += n


def fun(n):
    local.x = num
    for i in range(1000):
        run(local.x,n)
    print("%s --  %d" % (threading.current_thread().name,local.x))

if __name__ == "__main__":
    t1 = threading.Thread(target=fun,args=(1,))
    t2 = threading.Thread(target=fun,args=(2,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()