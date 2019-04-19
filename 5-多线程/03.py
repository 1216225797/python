import time
import _thread as thread

def A(run):
    print("func A start at:",time.ctime(),"and i am",run)
    time.sleep(4)
    print("func A end at:",time.ctime())


def B(eat):
    print("func B start at:",time.ctime(),"and i am",eat)
    time.sleep(2)
    print("func B end at:",time.ctime())

def main():
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为：start_new_thread
    # 参数两个，一个是需要运行的函数名，第二个是函数的参数作为元组使用，为空则使用空元组
    # 注意：如何函数只有一个参数，需要参数后有一个逗号
    print("All start at:",time.ctime())
    # A()
    # B()
    thread.start_new_thread(A,("running",))
    thread.start_new_thread(B,("eating",))
    print("All end at:",time.ctime())

if __name__ == "__main__":
    main()
    # 使用循环的目的是为了在A和B线程在跑的时候，让main程序等着它们
    while True:
        time.sleep(1)