import functions as func
import random
import time

a = []
b = []
c = []
f = open('shakersort.txt', 'w')
for i in range(100,1000,100):
    for i in range(i):
        a.append(i)
        b.append(1000 - i)
        c.append(random.randint(0,10000))
    #print(a)
    #print(b)
    #print(c)
    start = time.time()
    func.shaker(a)
    end1 = time.time() - start
    print(end1)
    start = time.time()
    func.shaker(b)
    end2 = time.time() - start
    print(end2)
    start = time.time()
    func.shaker(a)
    end3 = time.time() - start
    print(end3)
    f.write("{:<6d},{:<10f},{:<10f},{:<10f}\n".format(i, end1 * 1000, end2 * 1000, end3 * 1000))



