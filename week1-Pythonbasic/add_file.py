import os


def main():
    bottom = ['/home/shiyanlou/syl','/home/shiyanlou/syl/A', '/home/shiyanlou/syl/B', '/home/shiyanlou/syl/C']
    for item in bottom:
        os.mkdir(item)
        os.mknod(item+'/__init__'+'.py')
    return


if __name__ == '__main__':
    main()
