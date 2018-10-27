def shaker(a):   (0)
    left = 0        (1)
    right = len(a) - 1      (2)

    while left <= right:    (3)
        for i in range(left, right, +1):    (4)
            if a[i] > a[i + 1]: (5)
                swap = a[i] (6)
                a[i] = a[i+1]   (7)
                a[i+1] = swap   (8)
        right -= 1  (9)
        for i in range(right, left, -1):    (10)
            if a[i - 1] > a[i]: (11)
                swap = a[i]  (12)
                a[i] = a[i+1] (13)
                a[i+1] =swap (14)
                
        left += 1      (15)

ооьь