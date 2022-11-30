#!/bin/python3
if __name__=='__main__':
    from lib import *
    math_l={"2":"+","3":"-","4":"*"}
    while 1:
        while 1:
            clear()
            ask=str(input("""
    Please choose calculation method:
    1. Hình thang (trapezoid)
    2. Phép cộng ma trận (+)
    3. Phép trừ ma trận (-)
    4. Phép nhân ma trận (*)
    5. Nhân ma trận lên nhiều lần (x1,x2,...)
    6. Mã hóa string bằng ma trận
    7. Giải mã string bằng ma trận
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
            elif ask=="6":
                max=1
                break
            elif ask=="7":
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
print("[Ctrl + C to Exit]")
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
    except KeyboardInterrupt:
        print("\\nExiting...")
        exit()
sum_matrix=int(m{0}*n{0})
matrix{0}=matrix_initialization(m{0},n{0})
print_matrix({0},matrix{0})
while 1:
    ask1=str(input("Do you want input [matrix {0}]? [Y/n]: "))
    if ask1.lower()=="y":
        print()
        matrix{0}=input_matrix(m{0},n{0},int({0}))
        break
    elif ask1.lower()=="n":
        break""".format(str(choose)))
        del ask1
        if ask=="1":
            trapezoid(str(matrix0))
        elif ask=="2" or ask=="3" or ask=="4":
            answer=calc_matrix(str(matrix0),str(matrix1),str(math_l[str(ask)]))
            if (answer==False):
                continue
            print_matrix("answer",answer)
        elif ask=="5":
            answer=matrix_xx(str(matrix0))
            print_matrix("answer",answer)
        elif ask=="6":
            text=str(input("Input text: "))
            text2=encrypt_matrix(1,str(matrix0),str(text))
            if (text2==False):
                continue
            clear()
            print("Key: ")
            print_matrix("key",matrix0)
            print("Original text: {}".format(str(text)))
            print("Encrypted text: {}".format(str(text2)))
        elif ask=="7":
            text=str(input("Input Encrypted text: "))
            text2=encrypt_matrix(0,str(matrix0),str(text))
            if (text2==False):
                continue
            clear()
            print("Key: ")
            print_matrix("key",matrix0)
            print("Encrypted text: {}".format(str(text)))
            print("Decrypted text: {}".format(str(text2)))
        pause()