import functions as func
from random import randint
import numpy as np
import time

if __name__ == '__main__':
    f = open('check.txt', 'w')
    for i in range(101,500, 100):
        end1 = []
        end2 = []
        end3 = []
        for j in range(1,400):
            print(j)
            M, N, Q = i, i + 1, i
            a = [[randint(0, 25) for i in range(N)] for j in range(M)]
            b = [[randint(0, 25) for i in range(Q)] for j in range(N)]
            #print(a)
            #print(b)
            start = time.time()
            res = func.multiply(a, b, M, N, Q)
            end1.append(time.time() - start)
            #print(end1)
            #print(res)

            start = time.time()
            result_wino = func.winograd(a, b)
            end2.append(time.time() -start)
            #print(end2)
            #print(result_wino)

            start = time.time()
            result_opt = func.opt_winograd(a, b)
            end3.append(time.time() - start)
            #print(end3)
            #print(result_opt)
            #num = np.matmul(a, b)
            #print(num)
        average1 = sum(end1)/len(end1)
        average2 = sum(end2) / len(end2)
        average3 = sum(end3) / len(end3)
        f.write("{:<6d},{:<10f},{:<10f},{:<10f}\n".format(i, average1, average2, average3))