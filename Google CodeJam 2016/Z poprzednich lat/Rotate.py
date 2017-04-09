def reader(file):
    f = open(file,'r')
    f_out = file[:-2] + 'out'
    T = int(f.readline())
    cases = []
    Ks = []
    for t in range(T):
        case = []
        NK = list(eval(f.readline().replace(" ", ",")))
        N = NK[0]
        K = NK[1]
        Ks.append(K)
        for n in range(N):
            n_list = []
            n_line = f.readline()
            for n_el in n_line[:N]:
                n_list.append(n_el)
            case.append(n_list)
        cases.append(case)
    return cases, Ks, f_out

def solver(cases, Ks, f_out):
    moves = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
    f_out = open(f_out, 'w')
    for c in range(len(cases)):
        case = cases[c]
        for row in case:
            #print(row)
            for col in range(len(row)):
                col = len(row) - col - 1
                if row[col] == '.' and col:
                    for i in range(col):
                        if row[col] == '.':
                            del row[col]
                            row.insert(0, '.')
                        else:
                            break
            #print(row)
        K = Ks[c]
        #print(K)
        result = []
        for y in range(len(case)):
            for x in range(len(case[y])):
                color = case[y][x]
                if color not in result and color != '.':
                    for move in moves:
                        for a in range(1,K):
                            if (0 <= y + a*move[0] < len(case)) and (0 <= x + a*move[1] < len(case[y])):
                                temp_piece = case[y + a*move[0]][x + a*move[1]]
                                if temp_piece == color:
                                    if a == K-1:
                                        result.append(color)
                                else:
                                    break
                            else:
                                break
        #print(result)
           
        if 'B' in result:
            if 'R' in result:
                result_str = 'Both'
            else:
                result_str = 'Blue'
        elif 'R' in result:
            result_str = 'Red'
        else:
            result_str = 'Neither'
        print("Case #{}: {}".format(c+1,result_str), file = f_out)         

def main():
    cases, Ks, f_out = reader("A-large-practice.in")
    solver(cases, Ks, f_out)
    
                
                

main()

    
            
        
    
