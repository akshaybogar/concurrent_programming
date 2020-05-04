import threading
from readerwriterlock import rwlock

today = 0
weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
'saturday']

marker = rwlock.RWLockFair()

def weekday_reader(_id):
    global today
    read_marker = marker.gen_rlock()
    while today < len(weekdays)-1:
        read_marker.acquire()
        print('Reader-', str(_id), 'sees', weekdays[today], 'reader count - ', read_marker.c_rw_lock.v_read_count)
        read_marker.release()

def weekday_writer(_id):
    global today
    write_marker = marker.gen_wlock()
    while today < len(weekdays)-1:
        write_marker.acquire()
        today = (today+1) % 7
        print('Writer-', str(_id), 'day modifies to', weekdays[today])
        write_marker.release()

if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=weekday_reader, args=(i,)).start()
    for i in range(2):
        threading.Thread(target=weekday_writer, args=(i,)).start()
