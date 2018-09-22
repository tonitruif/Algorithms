import functions as func

if __name__ == '__main__':
    M1, N1 = 5, 4
    M2, N2 = 4, 6
    if N1 != M2:
        print('unable to multiply')
    else:
        a = []
        b = []
        func.create_matrix(M1, N1, a)
        func.create_matrix(M2, N2, b)
        print(a)
        print(b)