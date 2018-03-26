
from apscheduler.schedulers.background import BackgroundScheduler

def my_job(*arg):
    print("OKOKOKOK")

sched = BackgroundScheduler()
sched.add_job(my_job, 'cron', minute='*/20', hour='*', day='*', month='*', week='*',args=["张三", "王五", "李四"])
sched.start()