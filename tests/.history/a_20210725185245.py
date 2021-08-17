import schedule
import time

arr = ['React', 'Python', 'JS', 'PHP', 'anything']
def add_no(key):
    return print(key, ' got it')

for i, index in enumerate(arr):
    schedule.every(3).seconds.do(add_no, index)
    schedule.run_pending()
    time.sleep(1)
    print(i, ':', index)