import threading
import time

items_on_notepad = 0
pencil = threading.Lock()

def add_items_on_notepad():
    global items_on_notepad
    items_to_add = 0
    while items_on_notepad <=20:
        if (items_to_add and pencil.acquire(blocking=False)): #non-blocking lock
            print('{} is adding items'.format(threading.current_thread().getName()))
            items_on_notepad += items_to_add
            items_to_add = 0
            time.sleep(0.3) #300ms to write on notepad
            pencil.release()
        else:
            print('{} is searching if there are items to add'.format(threading.current_thread().getName()))
            time.sleep(0.1) #100ms to search items
            items_to_add += 1

if __name__ == '__main__':
    thread_a = threading.Thread(target=add_items_on_notepad)
    thread_b = threading.Thread(target=add_items_on_notepad)
    start_time = time.perf_counter()
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()
    elapsed_time = time.perf_counter() - start_time
    print('Threads took {:.2f} seconds to complete the job'.format(elapsed_time))
