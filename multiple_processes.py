import os
import threading
import multiprocessing as mp

def create_threads_or_processes():
    while True:
        pass

def print_threads():
    print('Process ID - {}'.format(os.getpid()))
    for thread in threading.enumerate():
        print(thread)

def create_ten_processes():
    print('\n Creating 10 processes')
    for i in range(10):
        mp.Process(target=create_threads_or_processes).start()

if __name__ == '__main__':
    print_threads()
    create_ten_processes()
    print_threads()
