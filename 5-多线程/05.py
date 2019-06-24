import time
import threading

def A(run):
    print("func A start at:",time.ctime(),"and i am",run)
    time.sleep(4)
    print("func A end at:",time.ctime())


def B(eat):
    print("func B start at:",time.ctime(),"and i am",eat)
    time.sleep(2)
    print("func B end at:",time.ctime())

def main():
    # 参数两个，target是需要运行的函数名，args是函数的参数作为元组使用，为空则使用空元组
    # 注意：如何函数只有一个参数，需要参数后有一个逗号
    print("All start at:",time.ctime())
    t1 = threading.Thread(target=A, args=("running",))
    t1.start()

    t2 = threading.Thread(target=B, args=("eating",))
    t2.start()
    t1.join()


    t2.join()
    print("All end at:",time.ctime())

if __name__ == "__main__":
    main()