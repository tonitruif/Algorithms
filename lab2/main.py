import functions as func
from random import randint
import numpy as np

if __name__ == '__main__':
    f = open('out.txt', 'w')
    for i in range():
        
    M,N,Q = 2, 3, 2
    a = [[randint(0,25) for i in range(N)] for j in range(M)]
    b = [[randint(0,25) for i in range(Q)] for j in range(N)]

    res = func.multiply(a, b, M, N, Q)
    print(res)
    result_wino = func.winograd(a,b)
    print(result_wino)
    result_opt = func.opt_winograd(a,b)
    print(result_opt)
    num = np.matmul(a,b)
    print(num)

    #res = func.matrixmult(a,b)
    #print(res)