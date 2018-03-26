# import itertools
# a= itertools.cycle('1234')
# b=[]
# for n in a:
#      print(n)


# while True:
#      print("1")
#      print("2")
#      print("3")
#      print("4")


# class Base:
#     def __init__(self):
#         print('This is Base init function')
# class A(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('This is init function of A')
#
# class B(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('This is init function of B')
#
# class C(B,A):
#     def __init__(self):
#         super().__init__()
#         # A.__init__(self)
#         # B.__init__(self)
#         print('This is init function of C')



class Base(object):
     def __init__(self):
          print("enter Base")
          print("leave Base")
#
#
class A(Base):
     def __init__(self):
          self.a=3
          print("enter A")
          super(A, self).__init__()
          print("leave A")
#
#
# class B(Base):
#      def __init__(self):
#           print("enter B")
#           super(B, self).__init__()
#           print("leave B")
#
#
# class C(A, B):
#      def __init__(self):
#           print("enter C")
#           super(C, self).__init__()
#           print("leave C")


import threading
import time

def countNum(n): # 定义某个线程要运行的函数
         print("running on number:%s" %n)


if __name__ == '__main__':

     for i in range(0, 10):
         t1 = threading.Thread(target=countNum,args=(i,)) #生成一个线程实例
         t1.start()

     import copy
     # my_test=C()
     # print(C.mro())
     # a=lambda x,y:x+y
     # print(a(2,3))
     #
     # list1=[123,123,1234,345,345,567]
     # print(set(list1))
     # b={}
     # b=b.fromkeys(list1)
     # print(list(b.keys()))
     #
     # a = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]
     # a.sort()
     # b = a
     # #.Python里面如何拷贝一个对象
     # import random
     # my_test1=A()
     # my_test2=my_test1
     # my_test2.a=7
     # print(my_test1.a)
     # print(random.randint(1,999999))
     # print(random.randrange(0,10))
     # print(random.choice(list1))
     # random.shuffle(list1)
     # print(list1)
