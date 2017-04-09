def reader(plik):
    f = open(plik)
    l_1 = int(f.readline())                             #liczba przypadków w pliku
    for i in range(l_1):                                #pętla dla przypadków
        li_2 = int(f.readline())                        #liczba klocków
        li_3 = f.readline()
        D = list(eval(li_3.replace(" ",",")))           #wysokości klocków
        li_4 = f.readline()
        X = list(eval(li_4.replace(" ",",")))
        X_2 = [0]
        for i in range(0,len(D)-1):
            X_2.append(X_2[i]+X[i])
        XD = list(zip(D,X_2))
        print(XD)
    return XD

Domino = reader('efe00.in')

def state(Domino):
    state = []
    for i in range(len(Domino)):
        state.append([])
        h = Domino[i][0]
        if i == 0:
            d_l = 0
            d_p = Domino[i+1][1] - Domino[i][1]
        elif i == len(Domino)-1:
            d_l = Domino[i][1] - Domino[i-1][1]
            d_p = 0
        else:
            d_l = Domino[i][1] - Domino[i-1][1]
            d_p = Domino[i+1][1] - Domino[i][1]
        if (h < d_l):
            state[-1].append(0)
        else:
            state[-1].append(1)
        if (h < d_p):
            state[-1].append(0)
        else:
            state[-1].append(1)
    print(state)
    return state

state = state(Domino)

def Push(Domino,state):
    #prawo
    p_flag = True
    p_push = []
    pos = [i[1] for i in Domino]
    a = 0
    while p_flag:
        if a in pos:
            p_a = pos.index(a)
            a_t = Domino[p_a][1]
            for i in range(a,a_t):
                
        
        
        
        
    
    
    
    


            
            
    
