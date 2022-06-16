"""
    每隔一分钟写一次时间
"""
import time


def print_logo_time():
    with open('log.txt', 'ab+') as rw:
        line_num = 0
        # 将文件的偏移放在文件首位置
        rw.seek(0, 0)
        # 获取当前文件有多少行，用于line_num(行号)的累计
        for _ in rw:
            line_num += 1
        while True:
            line_num += 1
            time.sleep(1)
            rw.write(('%d.%s\n' % (line_num, time.ctime())).encode())
            # 刷新数据到磁盘
            rw.flush()


if __name__ == '__main__':
    print_logo_time()
