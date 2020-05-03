import threading

balls = 0
bats = 0
pencil = threading.RLock()

def ball_count():
    global balls
    pencil.acquire()
    balls += 1
    pencil.release()

def bat_count():
    global bats
    pencil.acquire()
    bats += 1
    ball_count()
    pencil.release()

def shopper():
    for i in range(100):
        ball_count()
        bat_count()

if __name__ == '__main__':
    thread_a = threading.Thread(target=shopper)
    thread_b = threading.Thread(target=shopper)
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()
    print('Balls count -{} and Bats count -{}'.format(balls, bats))
