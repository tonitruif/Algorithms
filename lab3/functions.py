def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a

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

