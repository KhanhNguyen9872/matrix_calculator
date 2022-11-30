if (__name__=='lib2'):
    try:
        import numpy as np
    except:
        from os import system,os
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