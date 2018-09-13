from lab1 import functions as func
import time

if __name__ == "__main__":
    '''
    str1 = str(input("enter string1: "))
    str2 = str(input("enter string2: "))
    '''
    str1 = 'tartaara'
    str2 = 'otafra'
    str2 = 'l' + str2
    str1 = 'l' + str1
    if str1 > str2:
        str1, str2 = str2, str1

    start = time.time()
    basic_levenstein = func.levenstein(str1, str2)
    print('RESULT BASIC: ',basic_levenstein)
    end = time.time() - start
    print(end * 10000,'\n')

    start = time.time()
    demerau = func.demerau(str1, str2)
    print('RESULT DEMERAU: ', demerau)
    end = time.time() - start
    print(end * 10000)

    start = time.time()
    recursion = func.recursion(str1, str2)
    print('RESULT RECURSION: ', recursion)
    end = time.time() - start
    print(end * 10000)
