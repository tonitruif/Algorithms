from random import randint
import time
import threading
import numpy as np


def multiply(a, b, c, start, fin):
    n = len(a[0])
    m = len(b[0])
    for i in range(start, fin):
        for j in range(m):
            for k in range(n):
                c[i][j] = c[i][j] + a[i][k]*b[k][j]


def winograd(a, b, c, start, fin):
    m = len(a)
    n = len(a[0])
    t = n//2+1
    row_fact = [0 for x in range(m)]
    column_fact = [0 for x in range(len(b[0]))]

    for i in range(m):
        row_fact[i] = 0
        for j in range(1, t):
            row_fact[i] = row_fact[i] + a[i][2*j-2] * a[i][2*j-1]

    for i in range(start, fin):
        column_fact[i] = 0
        for j in range(1, t):
            column_fact[i] = column_fact[i] + b[2*j-2][i] * b[2*j-1][i]

    for i in range(m):
        for j in range(start, fin):
            c[i][j] = -row_fact[i] - column_fact[j]
            for k in range(1, t):
                c[i][j] = c[i][j] + (a[i][2*k-2]+b[2*k-1][j])*(a[i][2*k-1] + b[2*k-2][j])

    if (n % 2 == 1):
        for i in range(m):
            for j in range(start, fin):
                c[i][j] = c[i][j] + a[i][n-1]*b[n-1][j]


if __name__ == '__main__':
    f1 = open('multest.txt', 'w')
    f2 = open('winotest.txt', 'w')
    for leng in range(100, 807, 100):
        a = [[randint(0, 10) for i in range(leng)] for j in range(leng)]
        b = [[randint(0, 10) for i in range(leng)] for j in range(leng)]
        r = np.matmul(a,b)
        for threadn in [1,2,4,8]:
            timemul = []
            timewino = []
            testnum = 30
            for j in range(testnum):

                threads = []
                c = [[0 for p in range(leng)] for d in range(leng)]
                shag = leng / threadn
                end = shag
                start = 0
                for i in range(threadn):
                    threads.append(threading.Thread(target=multiply, args=(a, b, c, int(start), int(end))))
                    end += shag
                    start += shag
                tb = time.time()
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()
                timemul.append(time.time() - tb)


                threads = []
                c = [[0 for i in range(leng)] for j in range(leng)]
                shag = leng / threadn
                end = shag
                start = 0
                for i in range(threadn):
                    threads.append(threading.Thread(target=winograd, args=(a, b, c, int(start), int(end))))
                    end += shag
                    start += shag
                tb = time.time()
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()
                timewino.append(time.time() - tb)

            averagemul = sum(timemul) / testnum
            averagewino = sum(timewino) / testnum

            print('Умножение, размерность {} потоки {} время {}'.format(leng, threadn, averagemul))
            print('Виноград,размерность {} потоки {} время {}'.format(leng, threadn, averagewino))
            f1.write("{},{},{}\n".format(leng, threadn, averagemul))
            f2.write("{},{},{}\n".format(leng, threadn, averagewino))









