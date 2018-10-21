def multiply(a, b, l, m, n):
    answer = [[0 for i in range(n)] for j in range(l)]
    for i in range(l):
        for j in range(n):
            for k in range(m):
                answer[i][j] += a[i][k] * b[k][j]
    return answer

def winograd(G, H):
    a = len(G)
    b = len(H)
    c = len(H[0])
    mulU = [0 for i in range(a)]
    mulV = [0 for i in range(c)]
    R = [[0 for i in range(c)] for j in range(a)]

    for i in range(a):
        for j in range(0, b // 2, 1):
            mulU[i] = mulU[i] + G[i][2 * j] * G[i][2 * j + 1]

    for i in range(c):
        for j in range(0, b // 2, 1):
            mulV[i] = mulV[i] + H[2 * j][i] * H[2 * j + 1][i]

    for i in range(a):
        for j in range(c):
            R[i][j] = - mulU[i] - mulV[j]
            for k in range(0, b // 2, 1):
                R[i][j] = R[i][j] + ((G[i][2 * k] + H[2 * k + 1][j]) * (G[i][2 * k + 1] + H[2 * k][j]))
    if b % 2:
        for i in range(a):
            for j in range(c):
                R[i][j] = R[i][j] + G[i][b - 1] * H[b - 1][j]

    return R

def opt_winograd(G, H):
    a = len(G)
    b = len(H)
    c = len(H[0])
    d = b // 2
    mulU = [0 for i in range(a)]
    mulV = [0 for i in range(c)]
    R = [[0 for i in range(c)] for j in range(a)]

    for i in range(a):
        for j in range(d):
            mulU[i] += G[i][2 * j] * G[i][2 * j + 1]

    for i in range(c):
        for j in range(d):
            mulV[i] += H[2 * j][i] * H[2 * j + 1][i]

    for i in range(a):
        for j in range(c):
            R[i][j] = - mulU[i] - mulV[j]
            for k in range(d):
                index = 2 * k
                R[i][j] += ((G[i][index] + H[index + 1][j]) * (G[i][index + 1] + H[index][j]))
    if b % 2:
        for i in range(a):
            for j in range(c):
                R[i][j] += G[i][b - 1] * H[b - 1][j]

    return R
