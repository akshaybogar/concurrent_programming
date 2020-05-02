import threading
import time

def infinite_thread():
    while True:
        print('Cleaning the kitchen')
        time.sleep(1)

if __name__ == '__main__':
    cleaner = threading.Thread(target=infinite_thread)
    cleaner.daemon = True
    cleaner.start()

    print('Chef is cooking')
    time.sleep(0.5)

    print('Chef is cooking')
    time.sleep(0.7)

    print('Chef is done cooking')
