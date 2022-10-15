from os import system,name
from sys import exit
def clear():
    if name=='nt':
        system('cls')
    else:
        system('clear')
def matrix_initialization(m,n):
    matrix=[]
    for i in range(0,int(m),1):
        temp_matrix=[]
        for j in range(0,int(n),1):
            temp_matrix.append(int(0))
        matrix.append(temp_matrix)
    return matrix
def head_matrix(m,n,num):
    print(" 0 | [matrix {2}] | max column: {0} | max row: {1}".format(str(n),str(m),str(num)))
def left_matrix(i):
    print(f" {i} | ",end="")
def print_matrix(num_matrix,execute,m,n):
    exec("""global matrix{0}
matrix{0}={1}
head_matrix(m,n,num_matrix)
count=0
for i in range(0,int(m),1):
    left_matrix(i+1)
    for j in matrix{0}[i]:
        print(str(j),end=" ")
    print()""".format(str(num_matrix),str(execute)))
def input_matrix(m,n,num):
    passk=0
    count=1
    temp_matrix=[]
    head_matrix(m,n,num)
    while 1:
        left_matrix(count)
        try:
            temp_input=str(input())
            temp_input=[round(float(x),2) for x in temp_input.split()]
            if (len(temp_input)==int(n)):
                passk=1
            else:
                passk=0
        except KeyboardInterrupt:
            print("Exiting...")
            exit()
        except:
            passk=0
        if (passk==1):
            temp_matrix.append(temp_input)
            count+=1
        elif (passk==0):
            continue
        if (count==m+1):
            break
    return temp_matrix
def trapezoid(e,m,n):
    exec(f"""global matrix
matrix={e}""")
    print()
    one=-1
    for i in range(0,len(matrix[0]),1):
        if int(matrix[0][i])==0:
            continue
        else:
            one=int(i+1)
            break
    if one==-1:
        print("The first row of the matrix does not contain the first non-zero element")
        exit()
    else:
        loop_calc=1
        for row in range(1,len(matrix),1):
            for num in range(0,len(matrix[row]),1):
                if int(num)<int(one):
                    if int(matrix[row][num])==0:
                        continue
                    else:
                        for i in range(0,len(matrix),1):
                            if (int(i)==int(row)) or (int(matrix[i][num])==0) or (int(matrix[row][num])==0):
                                continue
                            else:
                                up=float(matrix[row][num])
                                down=float(matrix[i][num])
                                print("\n({4}) h{0} -> h{0} - ({1}/{2}) * h{3}".format(str(row+1),str(up),str(down),str(i+1),str(loop_calc)))
                                for j in range(0,len(matrix[row]),1):
                                    matrix[row][j]=float(matrix[row][j])-float(up/down)*float(matrix[i][j])
                                print_matrix(int(0),str(matrix),m,n)
                                loop_calc+=1
                else:
                    one=int(num+1)
                    break
        return matrix
def calc_matrix(a,b,m0,n0,m1,n1):
    exec(f"""global matrix0,matrix1
matrix0={a}
matrix1={b}""")
    print()
    print('===========')
    print()
    if (int(n0)==int(m1)):
        answer=[]
        for row in range(0,len(matrix0),1):
            temp=[]
            for j in range(0,len(matrix1[0]),1):
                calc="0"
                row2=0
                for i in range(0,len(matrix0[row]),1):
                    calc+="+{0}{2}{1}".format(str(matrix0[row][i]),str(matrix1[row2][j]),str(math))
                    row2+=1
                temp.append(float(eval(calc)))
            answer.append(temp)
        return answer
    else:
        print("Cannot calculator {0}x{1} and {2}x{3}".format(str(m0),str(n0),str(m1),str(n1)))
        exit()
def matrix_xx(e,m,n):
    exec(f"""global matrix
matrix={e}""")
    print()
    while 1:
        try:
            math=int(input("Input number you want to multiply [1-250]: "))
            if 0<math<251:
                break
            else:
                print("Limit [1-250]")
        except KeyboardInterrupt:
            print("Exiting...")
            exit()
        except:
            print("Please input number!")
            print("Example: 2")
    print()
    print('===========')
    print()
    for row in range(0,len(matrix),1):
        for column in range(0,len(matrix[row]),1):
            matrix[row][column]=float(matrix[row][column]*int(math))
    return matrix