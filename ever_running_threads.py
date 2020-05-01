import os
import threading

def ever_running_threads():
  while True:
    pass

def active_threads():
    print('Process id - {}'.format(os.getpid()))
    print('Thread count - {}'.format(threading.active_count()))
    for thread in threading.enumerate():
        print(thread)

def create_ten_threads():
    print('\n creating 10 ever running threads')
    for i in range(10):
        threading.Thread(target=ever_running_threads).start()

active_threads()
create_ten_threads()
active_threads()
