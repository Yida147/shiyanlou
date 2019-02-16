import os, time, random
from multiprocessing import Pool


def task(name):
    print('任务{}启动运行, 进程ID:{}'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('任务{}结束运行, 耗时:{:.2f}s'.format(name, (end - start)))


if __name__ == '__main__':
    print('当前为主进程,进程ID:{}'.format(os.getpid()))
    print('-----------------------------------')
    p = Pool(4)
    for i in range(1, 6):
        p.apply_async(task, args=(i,))
    p.close()
    print('开始运行子进程...')
    p.join()
    print('-----------------------------------')
    print('所有子进程运行完毕, 当前为主进程, 进程ID:{}'.format(os.getpid()))