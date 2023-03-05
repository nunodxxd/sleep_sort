import _thread
import time
import random

rand_list = [random.randint(0,100) for _ in range(100)]
print(rand_list)

def sleep_sort(i):
        time.sleep(i/100)
        print(i)

for i in rand_list:
        arg_tuple = (i,)
        _thread.start_new_thread(sleep_sort, arg_tuple)
