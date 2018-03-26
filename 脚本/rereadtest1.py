# #conding = utf-8
# a=1
# a={'a':1,'b':2,'c':3}
# b=[1,2,3,4,5,21]
# c=set(b)
# c.add(123)
# def func_add(a=2):
#     print((max(b)),a)
#
#
# # add=func_add
# # add('qweqwe')
#
#
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
# def person2(name, age,*, city):
#     print('name:', name, 'age:', age, '城市:', city)
#
# # person('Adam', 45, gender='M', job='Engineer')
# #
# # extra = {'city': 'Beijing', 'job': 'Engineer'}
# # person('Jack', 24, **extra)
# # person2('Jack', 24, tar=324, city='Beijing')
#
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
#
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
#
# def move(n, a, b, c):
#     if n == 1:
#         print('move', a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, b, c)
#         move(n-1, b, a, c)
#
# move(4, 'A', 'B', 'C')
#
#
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#
# print('L[0:3] =', L[0:3])
# print('L[:3] =', L[:3])
# print('L[1:3] =', L[1:3])
# print('L[-2:] =', L[-2:])
#
# R = list(range(100))
# print('R[:10] =', R[:10])
# print('R[-10:] =', R[-10:])
# print('R[10:20] =', R[10:20])
# print('R[:10:2] =', R[:10:2])
# print('R[::5] =', R[::5])
#
# from collections import Iterable
# if isinstance(L, Iterable):
#     print("OK")
# print(min(b))
#
# ls=(x for x in range(1,10000000))
# # for i in ls:
# #     print(i)
#
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         # yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# # for n in fib(6):
# #       print(n)
# f= abs
#
# def add(x, y, f):
#     return f(x) + f(y)
# print(add(-1,-3,f))
#
# from functools import
# def f1(x):
#     return x * x
# r = map(f1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# t = reduce()
# print(type(r))
# print(list(r))

#######################################
#对比图片S
#######################################
# from PIL import Image
# from PIL import ImageChops
# from PIL import ImageGrab
#
# import numpy as np
#
#
# def compare_images(path_one, path_two, diff_save_location):
#     image_one = Image.open(path_one)
#     image_two = Image.open(path_two)
#
#     diff = ImageChops.difference(image_one, image_two)
#
#     if diff.getbbox() is None:
#         # 图片间没有任何不同则直接退出
#         return
#     else:
#         diff.save(diff_save_location)
#
# import time
# beg = time.time()
# debug = False
# for i in range(10):
#     img = ImageGrab.grab((250, 161, 1141, 610))
#     img.show()
#     img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
# end = time.time()
# print(end - beg)

#######################################
#对比图片E
#######################################
from functools import reduce

def add(x,y):
    return x + y

print(reduce(add, [1,2,4,5]))
print(map(add,[1,2,4,5]))

import datetime
print(datetime.datetime.now())
