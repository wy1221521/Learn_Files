# from time import sleep, time
# import gc
#
#
# def mem(way=1):
#     print(time())
#     for i in range(10000000):
#         if way == 1:
#             pass
#         else:  # way 2, 3
#             del i
#
#     print(time())
#     if way == 1 or way == 2:
#         pass
#     else:  # way 3
#         gc.collect()
#     print(time())
#
#
#
# if __name__ == "__main__":
#     print("Test way 1: just pass")
#
#     mem(way=1)
#     sleep(20)
#     print(
#     "Test way 2: just del")
#     mem(way=2)
#     sleep(20)
#     print("Test way 3: del, and then gc.collect()")
#     mem(way=3)
#     sleep(20)

    # import gc
# import sys
#
# class CGcLeak(object):
#     def __init__(self):
#         self._text = '#' * 10
#
#     def __del__(self):
#         pass
#
# def make_circle_ref():
#     _gcleak = CGcLeak()
#     print ("_gcleak ref count0: %d" %(sys.getrefcount(_gcleak)))
#     del _gcleak
#     try:
#         print ("_gcleak ref count1 :%d" %(sys.getrefcount(_gcleak)))
#     except UnboundLocalError:           # 本地变量xxx引用前没定义
#         print ("_gcleak is invalid!")
# def test_gcleak():
#     gc.enable()                         #设置垃圾回收器调试标志
#     gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_STATS | gc.DEBUG_LEAK)
#
#     print ("begin leak test...")
#     make_circle_ref()
#
#     print ("\nbegin collect...")
#     _unreachable = gc.collect()
#     print ("unreachable object num:%d" %(_unreachable))
#     print ("garbage object num:%d" %(len(gc.garbage)) )  #gc.garbage是一个list对象，列表项是垃圾收集器发现的不可达（即垃圾对象）、但又不能释放(不可回收)的对象，通常gc.garbage中的对象是引用对象还中的对象。因Python不知用什么顺序来调用对象的__del__函数，导致对象始终存活在gc.garbage中，造成内存泄露 if __name__ == "__main__": test_gcleak()。如果知道一个安全次序，那么就可以打破引用焕，再执行del gc.garbage[:]从而清空垃圾对象列表
# if __name__ == "__main__":
#     test_gcleak()

import time
import asyncio
from io import  StringIO

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
f= StringIO()
f.write("我"
        "就"
        "把"
        "这"
        "个"
        "写"
        "入内存了我就把这个写入内存了我就把这个写入内存了我就把这个写入"
        "内存了")
print(f.getvalue())
while True:
    print("写入")
    f.write("我"
            "就"
            "把"
            "这"
            "个"
            "写"
            "入内存了我就把这个写入内存了我就把这个写入内存了我就把这个写入")