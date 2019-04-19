import time
import threading

sum = 0
num = 10000

def myAdd():
    global sum,num
    for i in range(num):
        sum += 1

def myJian():
    global sum, num
    for j in range(num):
        sum -= 1

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