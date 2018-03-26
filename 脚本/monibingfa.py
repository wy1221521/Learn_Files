# coding=utf-8
import requests

url='127.0.0.1:8000'
# response = requests.get(url,  timeout=5)
#
# print(response.status_code)
# print(response.text)
print("OKOK",url)



# import httplib, urllib
# from time import ctime
# import threading
# import csv
#
# postJson = {
# }
# # 定义需要进行发送的数据
# params = urllib.urlencode(postJson);
#
# # 定义一些文件头
# headers = {"Content-Type": "application/x-www-form-urlencoded",
#            "Connection": "Keep-Alive"
#            }
#
#
# # 创建请求函数
# def Clean():
#     # 接口的url
#     requrl = ""
#     # 连接服务器
#     conn = httplib.HTTPConnection("")
#     # 发送请求
#     conn.request(method="POST", url=requrl, body=params, headers=headers)
#     # 获取请求响应
#     response = conn.getresponse()
#     # 打印请求状态
#     print
#     response.status
#
#
# # 创建数组存放线程
# threads = []
# # 创建100个线程
# for i in range(100):
#     # 针对函数创建线程
#     t = threading.Thread(target=Clean, args=())
#     # 把创建的线程加入线程组
#     threads.append(t)
#
# print
# 'start:', ctime()
# if __name__ == '__main__':
#     # 启动线程
#     for i in threads:
#         i.start()
#         # keep thread
#     for i in threads:
#         i.join()
#
# print
# 'end:', ctime()
# # Url.close()

