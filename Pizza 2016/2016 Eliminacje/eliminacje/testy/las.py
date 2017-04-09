def reader(f):
    l_1 = int(f.readline())                             #liczba przypadków w pliku
    for i in range(l_1):                                #pętla dla przypadków
        li_1_temp = f.readline()                        #wymiary tablic jako string
        space = li_1_temp.index(" ")
        li_1 = [int(li_1_temp[:space]),int(li_1_temp[space+1:])]
        #li_1 = [int(li_1_temp[0]),int(li_1_temp[2])]    #wymiary tablicy
        M = []                                          #plansza gry
        for y in range(li_1[0]):                        #dla y-linii
            M.append([])                                #twórz nową linię
            li_2 = list(f.readline())                   #zczytaj pierwszą linię (str)
            for x in li_2[0:li_1[1]]:                   #dla str^ wczytaj kolumny
                M[y].append(x)
    #print(M)
    return M

def Copy(plane):
    """Funkcja kopiująca macierze"""
    output = []
    for x in range(len(plane)):
        output.append([])
        for y in range(len(plane[x])):
            output[x].append(plane[x][y])
    return output    

def Printer(M):
    """Drukowanie macierzy"""
    for i in M:
        print(i)
    print("\n")

def Printer_f(M,plik):
    plik = open(plik,'w')
    for i in M:
        for j in i:
            print(j,sep = '',end = "",file = plik)
        print("",file = plik)
    print("\n",file = plik)

def turn(a,dct):
    """Skręcanie"""
    k = 1
    if a == "L":
        k = -1
    dct = [dct[1]*k,dct[0]*(-k)]
    return dct

def move(pos,dct,move):
    """Idź przód/tył"""
    if move == "N":
        pos[0] += dct[0]
        pos[1] += dct[1]
    elif move == "W":
        pos[0] -= dct[0]
        pos[1] -= dct[1]
    return pos

def nose(M,pos,dct):
    nos = []
    for i in range(4):
        try:
            if (pos[0]+dct[0] >= 0) and (pos[1]+dct[1] >= 0):
                nos.append(M[pos[0]+dct[0]][pos[1]+dct[1]])
            else:
                nos.append(False)
        except IndexError:
            nos.append(False)
        dct = turn("P",dct)
    for i in range(len(nos)):
        if nos[i] == "x":
            nos[i] = True
        elif nos[i] == "#":
            nos[i] = False
        elif nos[i] == "C":
            nos[i] = True
        else:
            nos[i] = False
    return nos

def Turn_mark(m,pos,dct_t,M):
    if dct_t == [-1,0]:
        if m == "P":
            M[pos[0]][pos[1]] = str("/")
        else:
            M[pos[0]][pos[1]] = str("\\")
    elif dct_t == [0,1]:
        if m == "P":
            M[pos[0]][pos[1]] = "\\"
        else:
            M[pos[0]][pos[1]] = "/"
    elif dct_t == [0,-1]:
        if m == "P":
            M[pos[0]][pos[1]] = "\\"
        else:
            M[pos[0]][pos[1]] = "/"
    if dct_t == [1,0]:
        if m == "P":
            M[pos[0]][pos[1]] = "/"
        else:
            M[pos[0]][pos[1]] = "\\"
    return M[pos[0]][pos[1]]

def Solver(M):
    #Printer(M)
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] in ["v","<",">","^"]:
                start = [i,j]
                if M[i][j] == "v":
                    dct = [1,0]
                elif M[i][j] == "<":
                    dct = [0,-1]
                elif M[i][j] == ">":
                    dct = [0,1]
                elif M[i][j] == "^":
                    dct = [-1,0]
            elif M[i][j] == "C":
                finish = [i,j]
    pos = start[:]
    moves = ["N","P","W","L"]
    walk = []
    cross = True
    solution = []
    solved = False
    while pos != finish :
        A = nose(M,pos,dct)
        A_t = A.count(True)
        if A_t == 1:
            m = A.index(True)
            if m%2 == 0:
                if M[pos[0]][pos[1]] == "x":
                    M[pos[0]][pos[1]] = 0
                pos = move(pos,dct,moves[m])
            else:
                dct_t = dct[:]
                dct = turn(moves[m],dct)
                M[pos[0]][pos[1]] = Turn_mark(moves[m],pos,dct_t,M)
    return solution

def Clear(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if type(M[i][j]) is int:
                M[i][j] = "."
     

def D_Solve(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] in ["v","<",">","^"]:
                start_t = M[i][j] 
                start = [i,j]
                if M[i][j] == "v":
                    dct = [1,0]
                elif M[i][j] == "<":
                    dct = [0,-1]
                elif M[i][j] == ">":
                    dct = [0,1]
                elif M[i][j] == "^":
                    dct = [-1,0]
            elif M[i][j] == "C":
                finish = [i,j]
    a = 0
    M[start[0]][start[1]] = a
    while M[finish[0]][finish[1]] == "C":
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j] == a:
                    if a == 0:
                        M[i][j] = a
                        a += 1
                        M[i+dct[0]][j+dct[1]] = a
                    else:
                        for k in range(4):
                            try:
                                p_t = [i+dct[0],j+dct[1]]
                                if (p_t[0]>=0) and (p_t[1]>=0):
                                    if M[p_t[0]][p_t[1]] == "C":
                                        M[p_t[0]][p_t[1]] = a + 1
                                    elif (M[p_t[0]][p_t[1]] != "#"):
                                        if M[p_t[0]][p_t[1]] == ".":
                                            M[p_t[0]][p_t[1]] = a + 1
                                        if M[p_t[0]][p_t[1]] > a:
                                            M[p_t[0]][p_t[1]] = a + 1
                            except IndexError:
                                pass
                            dct = turn("P",dct)
        a += 1
    pos = [finish[0],finish[1]]
    m = [[1,0],[0,-1],[-1,0],[0,1]]
    M_max = len(M)*len(M[0])+1
    while pos != [start[0],start[1]]:
        M[pos[0]][pos[1]] = "x"
        dct = [1,0]
        n = []
        for k in m:
            try:
                p_t = [pos[0]+k[0],pos[1]+k[1]]
                if (p_t[0]>=0) and (p_t[1]>=0):
                    try:
                        n.append(int(M[p_t[0]][p_t[1]]))
                    except ValueError:
                        n.append(M_max)
                else:
                    n.append(M_max)
            except IndexError:
                n.append(M_max)
        dct = m[n.index(min(n))]
        pos = [pos[0]+dct[0],pos[1]+dct[1]]
    M[start[0]][start[1]] = start_t
    M[finish[0]][finish[1]] = "C"
    Printer(M)
    return M
                                
def main():
    for i in range(1,2):
        if i<10:
            plik = "las0"+str(i)+".in"
        else:
            plik = "las10.in"
        print(plik)
        #A = []
        plik_1 = plik[:-2] + "out"
        f = open(plik)
        plik_1 = open(plik_1,'w')
        l_1 = int(f.readline())                             #liczba przypadków w pliku
        for i in range(l_1):                                #pętla dla przypadków
            li_1_temp = f.readline()                        #wymiary tablic jako string
            space = li_1_temp.index(" ")
            li_1 = [int(li_1_temp[:space]),int(li_1_temp[space+1:])]
            M = []                                          #plansza gry
            for y in range(li_1[0]):                        #dla y-linii
                M.append([])                                #twórz nową linię
                li_2 = list(f.readline())                   #zczytaj pierwszą linię (str)
                for x in li_2[0:li_1[1]]:                   #dla str^ wczytaj kolumny
                    M[y].append(x)
            M = D_Solve(M)
            Clear(M)
            Solver(M)
            Clear(M)
            #A.append(M)
            for i in M:
                for j in i:
                    plik_1.write(j)
                plik_1.write("\n")
            plik_1.write("\n")
      #Printer_f(A,plik_1)
        
        
main()


    



