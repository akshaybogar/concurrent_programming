import threading

sushi_count = 500
spoon_a = threading.Lock()
spoon_b = threading.Lock()
spoon_c = threading.Lock()

def pick_sushi(name, first_spoon, sec_spoon):
    global sushi_count
    while sushi_count:
        first_spoon.acquire()
        sec_spoon.acquire()
        if sushi_count > 0:
            sushi_count -= 1
            print(name, 'took a piece of sushi', sushi_count, 'remaining')
        first_spoon.release()
        sec_spoon.release()

if __name__ == '__main__':
    #Remove deadlock by prioritising locks. highest-spoon_a,mid-spoon_b,low-spoon_c
    threading.Thread(target=pick_sushi, args=('A', spoon_a, spoon_b)).start()
    threading.Thread(target=pick_sushi, args=('B', spoon_b, spoon_c)).start()
    # To create deadlock
    # threading.Thread(target=pick_sushi, args=('C', spoon_c, spoon_a)).start()
    threading.Thread(target=pick_sushi, args=('C', spoon_a, spoon_c)).start()
