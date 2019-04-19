import time
import threading
def funcA():
    print("thread A start",time.ctime())
    time.sleep(3)
    print("thread A end",time.ctime())
def funcB():
    print("thread B start",time.ctime())
    time.sleep(4)
    print("thread B end",time.ctime())

def funcC():
    print("thread C start",time.ctime())
    time.sleep(5)
    print("thread C end",time.ctime())

def main():
    print("main thread start")

    t1 = threading.Thread(target=funcA, args=())
    t1.setName("thread_a")
    t1.start()
    t2 = threading.Thread(target=funcB, args=())
    t2.setName("thread_b")
    t2.start()
    t3 = threading.Thread(target=funcC, args=())
    t3.setName("thread_c")
    t3.start()

    time.sleep(3)
    # threading.enumerate()表示正在运行线程的列表
    for thr in threading.enumerate():
        print("正在运行的线程：",thr.getName())
    print("正在运行线程的数量:",threading.activeCount())
    print("main thread end")

if __name__ == "__main__":
    main()