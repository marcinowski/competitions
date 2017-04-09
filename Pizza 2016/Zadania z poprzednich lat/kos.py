def reader():
    A = []
    f = open('kos.txt')
    l_1 = int(f.readline())
    for i in range(l_1):
        li_1_temp = f.readline()
        li_1 = [int(li_1_temp[0]),int(li_1_temp[2])]
        M = []
        for y in range(li_1[0]):
            M.append([])
            li_2 = list(f.readline())
            for x in li_2[0:li_1[1]]:
                M[y].append(x) 
        A.append(M)
    return A

B = reader()
M = B[1]

def Printer(M):
    for i in M:
        print(i)
    print("\n")

def Test(M):
    solved = True
    for i in M:
        for j in i:
            if j == '.':
                solved = False
    return solved
        
def Solver(M):
    Printer(M)
    start = [0,0]
    dct = [0,1]
    pos = start[:]
    moves = ["N","P","W","L"]
    a = 0
    walk = []
    cross = False
    solution = []
    solved = False
    while not solved:
        M[pos[0]][pos[1]] = str(a)#lub a
        A = nose(pos,dct)
        A_t = A.count(True)
        if A_t == 1:
            m = A.index(True)
            if m%2 == 0:
                pos = move(pos,dct,moves[m])
            else:
                dct = turn(moves[m],dct)
            if cross == True:
                walk[-1].append(moves[m])
            solution.append(moves[m])
        elif A_t > 1:
            cross = True
            walk.append([])
            m = A.index(True)
            if m%2 == 0:
                pos = move(pos,dct,moves[m])
            else:
                dct = turn(moves[m],dct)
            if cross == True:
                walk[-1].append(moves[m])
            solution.append(moves[m])
        elif A_t == 0:
            pos,dct,sol_temp = reverse(walk[-1],pos,dct)
            a += len(walk[-1])
            del(walk[-1])
            for i in sol_temp:
                solution.append(i)
        Printer(M)
        a += 1
        solved = Test(M)
    print(solution)
    return solution

def reverse(walk,pos,dct):
    walk = walk[::-1]
    sol = []
    for i in walk:
        if i == "N":
            pos = move(pos,dct,"W")
            sol.append("W")
        elif i == "W":
            pos = move(pos,dct,"N")
            sol.append("N")
        elif i == "L":
            dct = turn("P",dct)
            sol.append("P")
        elif i == "P":
            dct = turn("L",dct)
            sol.append("L")
    return pos,dct,sol
    
def turn(a,dct):
    k = 1
    if a == "L":
        k = -1
    dct = [dct[1]*k,dct[0]*(-k)]
    return dct

def move(pos,dct,move):
    if move == "N":
        pos[0] += dct[0]
        pos[1] += dct[1]
    elif move == "W":
        pos[0] -= dct[0]
        pos[1] -= dct[1]
    return pos

def nose(pos,dct):
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
        if nos[i] == ".":
            nos[i] = True
        elif nos[i] == "#":
            nos[i] = False
        elif type(nos[i]) == str:
            nos[i] = False
        else:
            nos[i] = False
    return nos

solution = Solver(M)
time = 0
for i in solution:
    if i == "W" or i == "N":
        time += 1
    else:
        time += 3
print(time)
    
            
        
    
    
    


    
