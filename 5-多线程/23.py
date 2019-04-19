import multiprocessing
import time

# 设置哨兵问题
def consumer(input_q):
    print("into consumer:",time.ctime())
    while True:
        item = input_q.get()
        # 当获取到None时，跳出循环，不再获取
        if item is None:
            break
        print("pull",item,"out of q")
    print("out of consumer:",time.ctime())

def producer(seq,output_q):
    print("into producer:",time.ctime())
    for item in seq:
        output_q.put(item)
        print("put",item,"into q")
    print("out of producer:",time.ctime())

if __name__ == '__main__':

    q = multiprocessing.JoinableQueue()

    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.start()

    seq = [1, 2, 3, 4]
    producer(seq,q)

    q.put(None)
    cons_p.join()

