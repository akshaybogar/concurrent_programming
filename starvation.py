'''
Remove abandoned lock using try block
'''
import threading

sushi_count = 500
spoon_a = threading.Lock()
spoon_b = threading.Lock()
#spoon_c = threading.Lock()

def pick_sushi(name, first_spoon, sec_spoon):
    global sushi_count
    sushi_eaten = 0
    while sushi_count:
        with first_spoon:
            with sec_spoon:
                if sushi_count > 0:
                    sushi_count -= 1
                    sushi_eaten += 1
                    print(name, 'took a piece of sushi', sushi_count, 'remaining')
    print(name, 'ate', sushi_eaten)

if __name__ == '__main__':
    #More the number of threads, more the chances of threads starve
    for i in range(30):
        threading.Thread(target=pick_sushi, args=('A'+str(i), spoon_a, spoon_b)).start()
        threading.Thread(target=pick_sushi, args=('B'+str(i), spoon_a, spoon_b)).start()
        threading.Thread(target=pick_sushi, args=('C'+str(i), spoon_a, spoon_b)).start()
