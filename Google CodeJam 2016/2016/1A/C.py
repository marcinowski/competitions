def reader(file):
    f = open(file,'r')
    f_out = file[:-2]+"out"
    T = int(f.readline())
    cases = []
    for t in range(T):
        N = int(f.readline())
        case = f.readline().strip().split(' ')
        cases.append(case)
    return cases, f_out

def solver(cases, f_out):
    f_out = open(f_out,'w')
    for c in range(len(cases)):
        case = cases[c]
        #base = list(range(1,len(case)+1))
        for el in range(len(case)):
            case[el] = int(case[el])
        result = 0
        for i in range(len(case)):
            temp = []
            temp.append(i+1)
            cur = i + 1
            while True:
                cur = case[cur-1]
                if cur not in temp:
                    temp.append(cur)
                else:
                    temp.append(cur)
                    break
            if len(temp) > result:
                result = len(temp)
        print("Case #{}: {}".format(c+1, result))
        #print("Case #{}: {}".format(c + 1, result), file=f_out)
    f_out.close()

def main():
    cases, f_out = reader('C-small-attempt0.in')
    solver(cases, f_out)

main()