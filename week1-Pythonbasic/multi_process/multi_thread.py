import threading


def hello(name):
    print('当前为子线程, 线程ID: {}'.format(threading.get_ident()))
    print('Hello '+ name)


def main():
    print('当前为主线程, 线程ID: {}'.format(threading.get_ident()))
    print('------------------------------------------')
    t = threading.Thread(target=hello, args=('shiyanlou',))
    t.start()
    t.join()
    print('------------------------------------------')
    print('当前为主线程, 线程ID:{}'.format(threading.get_ident()))


if __name__ == '__main__':
    main()