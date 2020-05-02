import threading
import time

class ChefB(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print('ChefB starts making coffee decoction')
        time.sleep(3)
        print('ChefB is done making decoction')

if __name__ == '__main__':
    print('ChefA is partenering with ChefB to make coffee')
    chefb = ChefB()

    print('ChefA is requesting ChefB to start')
    chefb.start()

    print('ChefA boils milk in the mean time')
    time.sleep(1)

    print('ChefA waits for ChefB to finish')
    chefb.join()

    print('ChefA mixes decoction, milk and adds sugar. Coffee prepared!')
