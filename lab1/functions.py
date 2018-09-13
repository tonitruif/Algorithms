def levenstein(str1, str2):
    l1, l2 = len(str1), len(str2)

    if (l1 == 0) and (l2 == 0):
        return 0

    if ((l1 == 0) and (l2 > 0)):
        return l2

    if ((l1 > 0) and (l2 == 0)):
        return l1

    mtr = [[0 for x in range(l2)] for y in range(l1)]
    for i in range(l1):
        for j in range(l2):
            mtr[0][j] = j
            mtr[i][0] = i

    for i in range(1,l1):
        for j in range(1,l2):
            if (str1[i] == str2[j]):
                flagmatch = 0
            else:
                flagmatch = 1
            mtr[i][j] = min(mtr[i-1][j]+1, mtr[i][j-1]+1, mtr[i-1][j-1] + flagmatch)

    for i in range(l1):
        for j in range(l2):
            print(mtr[i][j], end = ' ')
        print()
    return mtr[i][j]


