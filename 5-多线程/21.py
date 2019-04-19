import multiprocessing
import os

def info(title):
    print(title)
    print('module_name',__name__)
    # 得到父进程ID
    print("parent_process",os.getppid())
    # 得到自身进程ID
    print('process_id',os.getpid())

def func(name):
    info('function func')
    print(name)

if __name__ == '__main__':
    info('main_proc')
    p = multiprocessing.Process(target=func, args=('hahha',))
    p.start()
    p.join()