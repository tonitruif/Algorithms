import functions as func

if __name__ == "__main__":
    str1 = str(input("enter string1: "))
    str2 = str(input("enter string2: "))
    str2 = 'l'+ str2
    str1 = 'l'+ str1
    if str1 > str2:
        str1, str2 = str2, str1

    func.levenstein(str1, str2)
