import sys
import socket

def get_args():
    args = sys.argv[1:]

    try:
        # 首先获得参数
        host_index = args.index('--host')
        port_index = args.index('--port')
        host_temp = args[host_index + 1]
        port_temp = args[port_index + 1]

        # 判断IP地址格式
        if len(host_temp.split('.')) != 4:
            raise ValueError()
        host = host_temp

        # 判断是否为单端口
        if '-' in port_temp:
            port = port_temp.split('-')
        else:
            port = [port_temp, port_temp]

        return host, [int(port[0]), int(port[1])]
    except (ValueError, IndexError):
        # 获取参数出错, 则打印错误信息并退出
        print('Parameter Error')
        exit()


def scan():
    host, port = get_args()

    open_list = []
    # 扫描端口
    for i in range(port[0], port[1]+1):
        s = socket.socket()
        # 设置超时,防止脚本卡住
        s.settimeout(0.1)
        if s.connect_ex((host, i)) == 0:
            open_list.append(i)
            print(i, 'open')
        else:
            print(i,'closed')

        s.close()

    # 输出处于开启状态的端口
    # print(f'Complted scan. Opening ports at {open_list}')
    # print(f'Complted scan. Opening ports at {open_list}')


# 执行
if __name__ == '__main__':
    scan()