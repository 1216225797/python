import multiprocessing
import time

def clock(sleep_time):
    while True:
        print(time.ctime())
        time.sleep(sleep_time)

if __name__ == "__main__":
    p = multiprocessing.Process(target = clock, args=(5,))
    p.start()

    while True:
        print('sleeping........')
        time.sleep(1)