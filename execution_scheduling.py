'''
This program creates 2 threads which chop vegetables
'''

import time
import threading

chop = True
def chop_vegetables():
    thread_name = threading.current_thread().getName()
    vegetables = 0
    while chop:
        print('{} is chopping a vegetable'.format(thread_name))
        vegetables += 1
    print('{} chopped {} vegetables'.format(thread_name, vegetables))

if __name__ == '__main__':
    threading.Thread(target=chop_vegetables, name='Thread-1').start()
    threading.Thread(target=chop_vegetables, name='Thread-2').start()
    time.sleep(1)
    chop=False
