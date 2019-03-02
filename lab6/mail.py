import threading
import time
import queue
import random


def level1():
    i = 1
    time_end = time.time() - timeBegin
    while time_end < 3:
        if not queue1.empty():
            f.write('взят на обработку в 1 очередь {}\n'.format(i))
            deleted = queue1.get()
            tmp1 = pow(deleted, 2)
            tmp2 = pow(deleted, 4)
            time.sleep(0.00001)
            f.write('поступил 2 в очередь {} {}\n'.format(tmp1,i))
            f.write('поступил 2 в очередь {} {}\n'.format(tmp2, i))
            mutex2.acquire()
            queue2.put(tmp1)
            queue2.put(tmp2)
            mutex2.release()
            i = i+1
        time_end = time.time() - timeBegin
    print('Level1 stop')


def level2():
    global timeBegin
    #time.sleep(0.001)
    time_end = time.time() - timeBegin
    print(time_end)
    i = 1
    while time_end < 3:
        if not queue2.empty():
            f.write('взят на обработку в 2 очередь {}\n'.format(i))
            mutex2.acquire()
            deleted = queue2.get()
            mutex2.release()
            tmp1 = pow(deleted, 6)
            tmp2 = pow(deleted, 8)
            mutex3.acquire()
            queue3.put(tmp1)
            queue3.put(tmp2)
            mutex3.release()
            f.write('поступил 3 в очередь {} {}\n'.format(tmp1, i))
            f.write('поступил 3 в очередь {} {}\n'.format(tmp2, i))
            i = i + 1
        time_end = time.time() - timeBegin
    print('LEVEL2 STOP')


def level3():
    global timeBegin
    #time.sleep(0.005)
    time_end = time.time() - timeBegin
    i = 1
    while time_end < 3:
        if not queue3.empty():
            mutex3.acquire()
            deleted = queue3.get()
            mutex3.release()

            result = deleted + 4
            f.write('закончил работу {} {}\n'.format(result, i))
            i = i + 1
        time_end = time.time() - timeBegin
    print('LEVEL 3 STOP')


if __name__ == '__main__':
    f = open('log.txt', 'w')
    threads = []
    queue1 = queue.Queue()
    for i in range(1,50):
        queue1.put(random.randint(1, 100))
    queue2 = queue.Queue()
    queue3 = queue.Queue()
    timeBegin = time.time()
    mutex1 = threading.Lock()
    mutex2 = threading.Lock()
    mutex3 = threading.Lock()
    t1 = threading.Thread(target=level1)
    t2 = threading.Thread(target=level2)
    t3 = threading.Thread(target=level3)
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

