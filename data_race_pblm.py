import threading

balls = 0
def add_balls():
    global balls
    for i in range(1000000):
        balls += 1

if __name__ == '__main__':
    thread_a = threading.Thread(target=add_balls)
    thread_b = threading.Thread(target=add_balls)
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()

    #Balls count should be 2000000 but due to data race problem, count is inconsistent
    print('Balls count {}'.format(balls))
