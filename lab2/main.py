import functions as func
from random import randint
import numpy as np

if __name__ == '__main__':
    M,N,Q = 2, 3, 2
    a = [[randint(0,25) for i in range(N)] for j in range(M)]
    b = [[randint(0,25) for i in range(Q)] for j in range(N)]
    #a = [[2,-3,1],[5,4,-2]]
    #b = [[-7,5], [2,-1],[4,3]]
    print(a)
    print(b)
    res = func.multiply(a, b, M, N, Q)
    print(res)
    result_wino = func.winograd(a,b)
    print(result_wino)
    num = np.matmul(a,b)
    print(num)

    #res = func.matrixmult(a,b)
    #print(res)