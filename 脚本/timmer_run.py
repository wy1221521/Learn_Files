# import time
# from apscheduler.schedulers.background import BackgroundScheduler
#
# def my_job(*args):
#     print("This is a test",args)
#
# if __name__ == '__main__':
#     sched = BackgroundScheduler()
#     sched.add_job(my_job, 'cron', minute='*', hour='*', day='*', month='*', week='*',args=["张三", "王五", "李四"] )
#     sched.start()
#     while True:
#         time.sleep(1)

import time
# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.schedulers.background import BackgroundScheduler
#
#
# def test_job():
#     print("This is a test")
#
# # scheduler = BlockingScheduler()
# scheduler = BackgroundScheduler()
# '''
# # 该示例代码生成了一个BlockingScheduler调度器，使用了默认的默认的任务存储MemoryJobStore，以及默认的执行器ThreadPoolExecutor，并且最大线程数为10。
# '''
# scheduler.add_job(test_job, 'interval', seconds = 1, id ='test_job')
# '''
# # 该示例中的定时任务采用固定时间间隔（interval）的方式，每隔5秒钟执行一次。
# # 并且还为该任务设置了一个任务id
# '''
# scheduler.start()
# coding=utf-8
# """
# Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
# intervals.
# """
#
# from datetime import datetime
# import time
# import os
#
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import os
import logging


def job_function():
    print("Hello World" + " " + str(datetime.now()))


if __name__ == '__main__':

    log = logging.getLogger('apscheduler.executors.default')
    log.setLevel(logging.INFO)  # DEBUG

    fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    h = logging.StreamHandler()
    h.setFormatter(fmt)
    log.addHandler(h)

    print('start to do it')

    sched = BackgroundScheduler()
    sched.add_job(job_function, 'interval', seconds=1)
    sched.start()
    while True:
        time.sleep(1)


