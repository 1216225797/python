import time
import threading
def funcA():
    print("thread start",time.ctime())
    time.sleep(2)
    print("thread end",time.ctime())

print("main thread start")
time.sleep(1)
t = threading.Thread(target=funcA, args=())
t.start()
print("main thread end")