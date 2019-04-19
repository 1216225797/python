import time
import threading

sum = 0
num = 10000
lock = threading.Lock()

def myAdd():
    global sum,num
    for i in range(num):
        # 申请锁
        lock.acquire()
        sum += 1
        # 释放锁
        lock.release()

def myJian():
    global sum, num
    for j in range(num):
        lock.acquire()
        sum -= 1
        lock.release()

def main():
    print("thread start...sum={}".format(sum))
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myJian, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    time.sleep(3)
    print("thread ended.......sum={}".format(sum))

if __name__ == '__main__':
    main()