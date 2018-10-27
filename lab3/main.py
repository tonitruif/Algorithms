import functions as func
import random
import time

a = []
b = []
c = []
f = open('qsort.txt', 'w')
for i in range(100,5000,500):
    for i in range(i):
        a.append(i)
        b.append(1000 - i)
        c.append(random.randint(0,10000))
    #print(a)
    #print(b)
    #print(c)
    start = time.time()
    func.insertion_sort(a)
    end1 = time.time() - start
    print(i,end1)
    start = time.time()
    func.insertion_sort(b)
    end2 = time.time() - start
    print(i,end2)
    start = time.time()
    func.insertion_sort(c)
    end3 = time.time() - start
    print(i,end3)
    print(c)
    f.write("{:<6d},{:<10f},{:<10f},{:<10f}\n".format(i, end1, end2, end3))



