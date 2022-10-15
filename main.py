#!/bin/python3
if (__name__=='__main__'):
    # import module
    import sys,lib
    # ask
    while 1:
        ask=str(input("""
Please choose calculation method:
1. Hình thang (trapezoid)
2. Nhân ma trận
Ctrl + C -> Exit

Your choose: """))
        if ask == "1":
            max=1
            break
        elif ask == "2":
            max=2
            break
    # clear terminal
    lib.clear()
    # main
    for choose in range(0,int(max),1):
        exec("""global matrix{0},m{0},n{0}
matrix{0}=[]""".format(str(choose)))
        # input m and n
        exec("""print()
print('===========')
while 1:
    try:
        print()
        m{0},n{0}=[int(x) for x in input("Input mXn ({0}): ").replace("X","x").split("x")]
        if (m{0}==0) or (n{0}==0):
            print("m and n must bigger than 0")
        else:
            break
    except ValueError:
        print('Please input mXn')
        print('Example: 3x5')
sum_matrix=int(m{0}*n{0})
# matrix initialization
matrix{0}=lib.matrix_initialization(m{0},n{0})
lib.print_matrix({0},matrix{0},m{0},n{0})
while 1:
    ask=str(input("Do you want input matrix ({0})? [Y/n]: "))
    if (ask=="Y") or (ask=="y"):
        print()
        matrix{0}=lib.input_matrix(m{0},n{0},int({0}))
        break
    elif (ask=="N") or (ask=="n"):
        break""".format(str(choose)))
    if max == 1:
        print()
        lib.trapezoid(str(matrix0),m0,n0)
    elif max == 2:
        print()
        print('===========')
        print()
        answer=lib.multiplication(str(matrix0),str(matrix1),m0,n0,m1,n1)
        lib.print_matrix("answer",answer,m0,n0)
