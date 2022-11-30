if (__name__=='lib'):
    try:
        from os import system,name
        from sys import exit
        import numpy as np
    except:
        if (os.name=='nt'):
            system('python -m pip install numpy')
        else:
            system('python3 -m pip install numpy')
        import numpy as np
    def ma_tran_con(mt, i, j):
        mt = np.delete(mt, i, 0);
        mt = np.delete(mt, j, 1);
        return mt

    def dinh_thuc(mt):
        so_chieu = mt.shape[1]
        if so_chieu == 1:
            return mt[0][0]
        ket_qua = 0
        j = 0
        while j < so_chieu:
            pds = ma_tran_con(mt, 0, j)
            ket_qua += ((-1) ** j) * mt[0][j] * dinh_thuc(pds)
            j = j + 1
            pass
        return ket_qua

    def nghich_dao(e):
        global mt
        exec(f"""global mt
mt={e}""")
        mt=np.array(mt)
        d_mt = dinh_thuc(mt)
        if d_mt == 0:
            return None
        so_hang = mt.shape[0]
        so_cot =  mt.shape[1]
        c = np.zeros(shape=(so_hang, so_cot))
        i = 0
        while i < so_hang:
            j = 0
            while j < so_cot:
                pds = ma_tran_con(mt, i, j)
                c[i][j] = ((-1) ** (i + j)) * dinh_thuc(pds)
                j = j + 1
            i = i + 1

        k = -1 / d_mt
        c_t = c.transpose()
        ket_qua = np.multiply(c_t, k)
        for i in range(0,len(ket_qua),1):
            for j in range(0,len(ket_qua[i]),1):
                ket_qua[i][j]=float(-ket_qua[i][j])
        return np.array(ket_qua).tolist()
    def error(m,n,text,errorat,required,error):
        print("Matrix size: {0}x{1}".format(str(m),str(n)))
        print("Text: \"{0}\" ({1} character)".format(str(text),str(len(text))))
        print("Error at: {}".format(str(errorat)))
        print("Required: {}".format(str(required)))
        print("ERROR: {}".format(str(error)))
    def clear():
        if name=='nt':
            system('cls')
        else:
            system('clear')
    def pause():
        input("\nPress Enter to Exit!")
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
    def print_matrix(num_matrix,execute):
        exec("""global matrix{0}
matrix{0}={1}
m=len(matrix{0})
n=len(matrix{0}[0])
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
    def trapezoid(e):
        exec(f"""global matrix
matrix={e}""")
        m,n=len(matrix),len(matrix[0])
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
                                    print_matrix(int(0),str(matrix))
                                    loop_calc+=1
                    else:
                        one=int(num+1)
                        break
            return matrix
    def calc_matrix(a,b,math):
        exec(f"""global matrix0,matrix1
matrix0={a}
matrix1={b}""")
        try:
            m0,n0=len(matrix0),len(matrix0[0])
            m1,n1=len(matrix1),len(matrix1[0])
        except TypeError:
            clear()
            error(0,0,"","MATH Error!","Try another matrix!","The program cannot calculator the matrix because the matrix is faulty!")
            pause()
            return False
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
    def matrix_xx(e):
        exec(f"""global matrix
matrix={e}""")
        m,n=len(matrix),len(matrix[0])
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
    def encrypt_matrix(k,e,text_ori):
        text2num={}
        num2text={}
        count=0
        khanhnguyen9872=0
        ## Character list
        character="-abcdefghijklmnopqrstuvwxyz"
        for char in character:
            text2num[str(char)]=int(count)
            num2text[int(count)]=str(char)
            count+=1
        len_char=len(character)
        global matrix
        exec(f"""global matrix
matrix={e}""")
        m=len(matrix)
        n=len(matrix[0])
        print()
        if (k!=0):
            text=text_ori.replace(" ","-")
        else:
            text=text_ori
        text2list=[]
        for i in range(0,len(matrix),1):
            text2list.append([])
        count=0
        while (count != len(text)):
            for i in range(0,len(matrix),1):
                try:
                    text2list[i].append(text2num[text[count].lower()])
                except KeyError:
                    clear()
                    error(m,n,text_ori,"Character \"{0}\" at count {1} in string!".format(str(text[count].lower()),str(count+1)),"Add \"{}\" to character list!".format(str(text[count].lower())),
                        "The program cannot encrypt this text because the text has a character not found in the character list!")
                    print("Character list: "+str(character))
                    pause()
                    return False
                except IndexError:
                    if (khanhnguyen9872==0):
                        len_t=len(text_ori)
                        while (len_t%len(matrix) != 0):
                            len_t+=1
                        while 1:
                            clear()
                            error(m,n,text_ori,"Only have {} character in string!".format(str(len(text_ori))),"{} character".format(str(len_t)),
                                "The program cannot encrypt this text because the text does not have enough characters with the matrix!")
                            print("\n SYSTEM: The program can fix it by adding space to your text!\n")
                            ask=str(input("Do you want to fix it? [Y/N]: "))
                            if (ask.lower()=="y"):
                                khanhnguyen9872=1
                                break
                            elif (ask.lower()=="n"):
                                return False
                    text2list[i].append(0)
                    text+="-"
                count+=1
        khanhnguyen9872=0
        if (k==0):
            matrix=nghich_dao(str(matrix))
        text2list=calc_matrix(str(matrix),str(text2list),"*")
        if (text2list==False):
            return False
        for row in range(0,len(text2list),1):
            for column in range(0,len(text2list[row]),1):
                while (text2list[row][column]>len_char-1):
                    text2list[row][column]-=len_char
                while (text2list[row][column]<0):
                    text2list[row][column]+=len_char
                try:
                    text2list[row][column]=num2text[text2list[row][column]]
                except KeyError:
                    if (khanhnguyen9872==0) and (k==0):
                        while 1:
                            clear()
                            error(m,n,text_ori,"\"{0}\" at {1}x{2} in matrix!".format(str(text2list[row][column]),str(row+1),str(column+1)),"Try encrypt another text or using another key",
                                "The program could not decrypt this text because when calculating the matrix, the program returned a float!")
                            print("\n SYSTEM: The program can ignore all these errors and continue running!\n")
                            ask=str(input("Do you want to continue? [Y/N]: "))
                            if (ask.lower()=="y"):
                                khanhnguyen9872=1
                                break
                            elif (ask.lower()=="n"):
                                return False
                    text2list[row][column]=num2text[int(text2list[row][column])]
        text=""
        for column in range(0,len(text2list[0]),1):
            for row in range(0,len(text2list),1):
                text+=str(text2list[row][column])
        if (k==0):
            text=text.replace("-", " ")
        return text