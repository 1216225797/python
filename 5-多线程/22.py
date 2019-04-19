import multiprocessing
import time

def consumer(input_q):
    print("into consumer:",time.ctime())
    while True:
        # 处理项
        item = input_q.get()
        print("pull",item,"out of q")
        # 发出信号通知任务完成
        input_q.task_done()
    # 此句未执行，因为q.join()收集到四个task_done()信号后
    # 主进程启动，未等到print此句完成，程序就结束了
    print("out of consumer:",time.ctime())

def producer(seq,output_q):
    print("into producer:",time.ctime())
    for item in seq:
        output_q.put(item)
        print("put",item,"into q")
    print("out of producer:", time.ctime())
# 建立进程
if __name__ == "__main__":
    q = multiprocessing.JoinableQueue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target=consumer,args=(q,))
    # 是否为守护进程
    cons_p.daemon = True
    cons_p.start()

    # 生产多个项，seq代表要发送给消费者的项序列
    # 在实践中，这可能是生成器的输出或通过一些其他方式生产出来

    seq = [1,2,3,4]
    producer(seq, q)
    q.join()