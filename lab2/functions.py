from random import randint


def create_matrix(m, n, a):
    for i in range(m):
        for j in range(n):
            a.append(randint(1, 25))
    return a