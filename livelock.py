'''
Program that creates a livelock
Here each thread tries to release the first lock if second lock cannot be
acquired potentially trying to resolve deadlock. This instead results in a
liveock
'''
import threading

sushi_count = 500
spoon_a = threading.Lock()
spoon_b = threading.Lock()
spoon_c = threading.Lock()

def pick_sushi(name, first_spoon, sec_spoon):
    global sushi_count
    while sushi_count:
        first_spoon.acquire()
        if not sec_spoon.acquire(blocking=False):
            print(name, 'releasing first spoon')
            first_spoon.release()
        else:
            try:
                if sushi_count > 0:
                    sushi_count -= 1
                    print(name, 'took a piece of sushi', sushi_count, 'remaining')
            finally:
                first_spoon.release()
                sec_spoon.release()

if __name__ == '__main__':
    threading.Thread(target=pick_sushi, args=('A', spoon_a, spoon_b)).start()
    threading.Thread(target=pick_sushi, args=('B', spoon_b, spoon_c)).start()
    threading.Thread(target=pick_sushi, args=('C', spoon_c, spoon_a)).start()
