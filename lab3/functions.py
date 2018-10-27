def bubble_sort(a):
    n = len(a)
    for i in range(n): # 2+N(2 +n-1(13 + 3))
        for j in range(n - 1, i, -1):
            if a[j] < a[j-1]:#4
                swap = a[j] #2     body = 13
                a[j] = a[j-1] #4
                a[j-1] = swap #3

    return #worse 18N^2 - 12, best: 2+N(2 + (N-1)(4+3) = 7N^2-3
def insertion_sort(a):
    for n in range(1,len(a)):
        i = n - 1
        while (i > -1) and a[i+1] < a[i]:
            a[i+1], a[i] = a[i], a[i+1]
            i -= 1
    return(a)
def shaker(a):
    left = 0
    right = len(a) - 1

    while left <= right:
        for i in range(left, right, +1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        right -= 1

        for i in range(right, left, -1):
            if a[i - 1] > a[i]:
                a[i], a[i - 1] = a[i - 1], a[i]
        left += 1

