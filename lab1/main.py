from lab1 import functions as func
import time
from memory_profiler import profile



if __name__ == "__main__":

    #str1 = str(input("enter string1: "))
    #str2 = str(input("enter string2: "))
    f = open('output.txt', 'w')
    str1 = 'aп'
    str2 = 'aa'
    f.write("column1, column2\n")
    for i in range(1,5):
        str1 += 'a'
        str2 += 'v' \
                ''
        str2 = 'l' + str2
        str1 = 'l' + str1
        if str1 > str2:
            str1, str2 = str2, str1
        print(len(str1))
        start = time.time()
        basic_levenstein = func.levenstein(str1, str2)
        print('RESULT BASIC: ',basic_levenstein)
        end1 = time.time() - start
        print(end1 * 10000,'\n')


        start = time.time()
        demerau = func.demerau(str1, str2)
        print('\nRESULT DEMERAU: ', demerau)
        end2 = time.time() - start
        print(end2 * 10000)
        print('\n\n\n')

        start = time.time()
        recursion = func.recursion(str1, str2)
        print('\nRESULT RECURSION: ', recursion)
        end3 = time.time() - start
        print(end3 * 10000)
        f.write("{:<6d},{:<10f},{:<10f},{:<10f}\n".format(len(str1), end1 * 1000, end2 * 1000, end3 * 1000))

    f.close()
