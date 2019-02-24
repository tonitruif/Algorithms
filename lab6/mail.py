import threading
import time
import queue
import random


def level1():
    i = 1
    time_end = time.time() - timeBegin
    while time_end < 3:
        if not queue1.empty():
            mutex1.acquire()
            deleted = queue1.get()
            mutex1.release()
            tmp1 = pow(deleted, 2)
            print('поступил в 1 очередь {} {}'.format(tmp1, i))
            mutex2.acquire()
            queue2.put(tmp1)
            mutex2.release()
            i = i+1
        time_end = time.time() - timeBegin
    print('Level1 stop')


def level2():
    global timeBegin
    time.sleep(0.001)
    time_end = time.time() - timeBegin
    print(time_end)
    i = 1
    while time_end < 3:
        if not queue2.empty():
            mutex2.acquire()
            deleted = queue2.get()
            mutex2.release()
            tmp1 = deleted + 1
            mutex3.acquire()
            queue3.put(tmp1)
            mutex3.release()
            print('закончил с 2 очередь {} {}'.format(tmp1, i ))
            i = i + 1
        time_end = time.time() - timeBegin
    print('LEVEL2 STOP')


def level3():
    global timeBegin
    time.sleep(0.005)
    time_end = time.time() - timeBegin
    i = 1
    while time_end < 3:
        if not queue3.empty():
            mutex3.acquire()
            deleted = queue3.get()
            mutex3.release()

            result = deleted + 4
            print('закончил работу {} {}'.format(result, i))
            i = i + 1
        time_end = time.time() - timeBegin
    print('LEVEL 3 STOP')


if __name__ == '__main__':
    threads = []
    queue1 = queue.Queue()
    logger1 = []
    for i in range(1,50):
        queue1.put(random.randint(1, 100))
    queue2 = queue.Queue()
    logger2 = []
    queue3 = queue.Queue()
    logger3 = []
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

