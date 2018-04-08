import threading


num = 0
lock = threading.Lock()

def run(n):
    global num
    with lock:
        num += n
        num -= n
'''   lock.acquire()
    try:
        num += n
        num -= n
    finally:
        lock.release()
'''
    #与上述功能相同，简写


if __name__ == "__main__":
    t1 = threading.Thread(target=run,args=(1,))
    t2 = threading.Thread(target=run,args=(2,))

    t1.start()
    t2.start()


    t1.join()
    t2.join()