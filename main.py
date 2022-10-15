#!/bin/python3
if __name__=='__main__':
    from lib import clear,matrix_initialization,print_matrix,input_matrix,trapezoid,calc_matrix,matrix_xx,exit
    clear()
    while 1:
        ask=str(input("""
Please choose calculation method:
1. Hình thang (trapezoid)
2. Phép cộng ma trận (+)
3. Phép trừ ma trận (-)
4. Phép nhân ma trận (*)
5. Nhân ma trận lên nhiều lần (x1,x2,...)
K. Exit

Your choose: """))
        if ask=="1":
            max=1
            break
        elif ask=="2":
            max=2
            break
        elif ask=="3":
            max=2
            break
        elif ask=="4":
            max=2
            break
        elif ask=="5":
            max=1
            break
        elif ask=="K" or ask=="k":
            print("Exiting...")
            exit()
    clear()
    for choose in range(0,int(max),1):
        exec("""global matrix{0},m{0},n{0}
matrix{0}=[]""".format(str(choose)))
        # input m and n
        exec("""print()
print('===========')
while 1:
    try:
        print()
        m{0},n{0}=[int(x) for x in input("Input mXn [matrix {0}]: ").replace("X","x").split("x")]
        if m{0}==0 or n{0}==0:
            print("m and n must bigger than 0")
        else:
            break
    except ValueError:
        print('Please input mXn')
        print('Example: 3x5')
sum_matrix=int(m{0}*n{0})
matrix{0}=matrix_initialization(m{0},n{0})
print_matrix({0},matrix{0},m{0},n{0})
while 1:
    ask1=str(input("Do you want input [matrix {0}]? [Y/n]: "))
    if ask1=="Y" or ask1=="y":
        print()
        matrix{0}=input_matrix(m{0},n{0},int({0}))
        break
    elif ask1=="N" or ask1=="n":
        break""".format(str(choose)))
    del ask1
    if ask=="1":
        trapezoid(str(matrix0),m0,n0)
    elif ask=="2":
        answer=calc_matrix(str(matrix0),str(matrix1),m0,n0,m1,n1,"*")
        print_matrix("answer",answer,m0,n0)
    elif ask=="3":
        answer=calc_matrix(str(matrix0),str(matrix1),m0,n0,m1,n1,"+")
        print_matrix("answer",answer,m0,n0)
    elif ask=="4":
        answer=calc_matrix(str(matrix0),str(matrix1),m0,n0,m1,n1,"-")
        print_matrix("answer",answer,m0,n0)
    elif ask=="5":
        answer=matrix_xx(str(matrix0),m0,n0)
        print_matrix("answer",answer,m0,n0)