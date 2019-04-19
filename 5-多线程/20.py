import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    '''
    两个函数比较重要
    1. init()构造函数
    2. run()
    '''
    def __init__(self, time_sleep):
        super().__init__()
        self.time_sleep = time_sleep

    def run(self):
        while True:
            print(time.ctime())
            time.sleep(self.time_sleep)

if __name__ == "__main__":
    c = ClockProcess(2)
    c.start()

    while True:
        print("sleep..........")
        time.sleep(1)