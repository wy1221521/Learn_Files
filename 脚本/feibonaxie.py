#
# i, j = 0, 1
# while i < 1000000000:
#     print( i)
#     i, j = j, i+j

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 10000: # 退出循环的条件
#             raise StopIteration()
#         return self.a
#
# for i in Fib():
#     print(i)
import sys
print(sys.getsizeof(1))