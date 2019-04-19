import threading
import time

# 1. 继承threading.Thread类
class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg
    # 2. 必须重写run函数，run函数代表真正执行的功能
    def run(self):
        time.sleep(2)
        print("我是参数{},哈哈哈！".format(self.arg))

for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()
print("Main thread is done")