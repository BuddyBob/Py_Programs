import schedule
import time
def job1():
    print(x)
def job2():
    print(y)

schedule.every(5).minutes.do(job1)
schedule.every(6).minutes.do(job2)
while True:
    schedule.run_pending()
    time.sleep(1)