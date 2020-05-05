import threading
import time
from random import random

sushi_count = 500
spoon_a = threading.Lock()
spoon_b = threading.Lock()
spoon_c = threading.Lock()

def pick_sushi(name, first_spoon, sec_spoon):
    global sushi_count
    while sushi_count > 0:
        first_spoon.acquire()
        if not sec_spoon.acquire(blocking=False):
            print(name, 'releasing first spoon')
            first_spoon.release()
            time.sleep(random()/10)
        else:
            try:
                if sushi_count > 0:
                    sushi_count -= 1
                    print(name, 'took a piece of sushi', sushi_count, 'remaining')
            finally:
                sec_spoon.release()
                first_spoon.release()

if __name__ == '__main__':
    threading.Thread(target=pick_sushi, args=('A', spoon_a, spoon_b)).start()
    threading.Thread(target=pick_sushi, args=('B', spoon_b, spoon_c)).start()
    threading.Thread(target=pick_sushi, args=('C', spoon_c, spoon_a)).start()
