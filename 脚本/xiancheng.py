#!/usr/bin/python
# compare for multi threads
import time

import threading


def worker():
    print("开始写文件")
    f=open("D:/test.txt", 'a+')
    f.write("OKOKOKOKOKOK")
    f.close()
    return

#
# if __name__ == "__main__":
#     for i in range(5):
#         worker()


# !/usr/bin/python


for i in range(5):
    t = threading.Thread(target=worker)
    t.start()