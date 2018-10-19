import functions as func
from random import randint
import numpy as np
import time

if __name__ == '__main__':
    f = open('out.txt', 'a')
    for i in range(2, 300, 25):
        M, N, Q = i, i + 1, i

        a = [[randint(0, 25) for i in range(N)] for j in range(M)]
        b = [[randint(0, 25) for i in range(Q)] for j in range(N)]

        start = time.time()
        res = func.multiply(a, b, M, N, Q)
        end1 = time.time() - start
        print(end1 * 1000)
        #print(res)

        start = time.time()
        result_wino = func.winograd(a, b)
        end2 = time.time() -start
        print(end2 * 1000)
        #print(result_wino)

        start = time.time()
        result_opt = func.opt_winograd(a, b)
        end3 = time.time() - start
        print(end3 * 1000)
        #print(result_opt)
        #num = np.matmul(a, b)
        #print(num)
        f.write("{:<6d},{:<10f},{:<10f},{:<10f}\n".format(i, end1 * 1000, end2 * 1000, end3 * 1000))