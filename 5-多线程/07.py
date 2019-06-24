import time
import threading
def funcA():
    print("thread start",time.ctime())
    time.sleep(2)
    print("thread end",time.ctime())

print("main thread start")
time.sleep(1)
t = threading.Thread(target=funcA, args=())
# 设置子线程为守护线程
# 必须要在启动前设置
t.setDaemon(True)

t.start()

print("main thread end")