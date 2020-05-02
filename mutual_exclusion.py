import threading

counter = threading.Lock()
balls = 0
def ball_count():
    counter.acquire()
    global balls
    for i in range(5):
        print(threading.current_thread().getName(), 'is updating balls count')
        balls += 1
    counter.release()

if __name__  == '__main__':
    thread_a = threading.Thread(target=ball_count)
    thread_b = threading.Thread(target=ball_count)
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()
    print('Balls count ', balls)
