def reader(file):
    f_out = file[:-2] + "out"
    f = open(file,'r')
    T = int(f.readline())
    cases = []
    for t in range(T):
        D = int(f.readline())
        P = f.readline().split(" ")
        for i in range(len(P)):
            P[i] = int(P[i])
        cases.append(P)
    return cases, f_out

def solver(cases, f_out):
    f_out = open(f_out, 'w')
    for c in range(len(cases)):
        case = cases[c]
        time = 0
        while len(case) != 0:
            #print(case)
            c_max = max(case)
            c_max_ind = case.index(c_max)
            if c_max > 3 and case.count(c_max) <= c_max:
                    rest = c_max - c_max//2
                    case.append(rest)
                    case[c_max_ind] = c_max//2
            else:
                for a in range(len(case)):
                    case[a] -= 1
            #print(case)
            while 0 in case:
                case.remove(0)
            time += 1
            #print(time)
        print("Case #{}: {}".format(c+1, time), file = f_out)

def main():
    cases, f_out = reader("B-small-practice.in")
    solver(cases, f_out)

main()
            
                    
                    
                
                
    
        
