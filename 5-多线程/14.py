import time
import threading

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def funcA():
    lock_1.acquire()
    print("funcA申请了锁1")
    time.sleep(4)
    print("funcA等待了锁2")
    lock_2.acquire()
    print("funcA申请了锁2")

    lock_2.release()
    print("funcA释放了锁2")
    lock_1.release()
    print("funcA释放了锁1")


def funcB():
    lock_2.acquire()
    print("funcB申请了锁2")
    time.sleep(4)
    print("funcB等待了锁1")
    lock_1.acquire()
    print("funcB申请了锁1")

    lock_1.release()
    print("funcB释放了锁1")
    lock_2.release()
    print("funcB释放了锁2")

if __name__ == "__main__":
    print("主程序启动")
    t1 = threading.Thread(target=funcA, args=())
    t2 = threading.Thread(target=funcB, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主程序结束")