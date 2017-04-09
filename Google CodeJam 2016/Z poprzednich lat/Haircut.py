def reader(file):
    f_out = file[:-2]+'out'
    f = open(file, 'r')
    T = int(f.readline())
    cases = []
    for t in range(T):
        BN = f.readline().strip().split(' ')
        case = f.readline().strip().split(' ')
        case.insert(0, BN[1])
        for c in range(len(case)):
            case[c] = int(case[c])
        cases.append(case)
    return cases, f_out

def min_div(lst):
    k = min(lst)
    min_div = 1
    if k >= 2:
        for i in range(1,k+1):
            f = True
            for a in lst:
                if a%i != 0:
                    f = False
                    break
            if f:
                min_div = i
    return min_div

def max_mult(lst):
    if len(lst) > 2 and type(lst[1]) != 'ínt':
        return max_mult([lst[0], max_mult(lst[1:])])
    elif len(lst) == 2 and type(lst[1] == 'int'):
        div = min_div(lst)
        mult = lst[0]*lst[1]
        return int(mult//div)

def solver(cases, f_out):
    f_out = open(f_out, 'w')
    for c in range(len(cases)):
        case = cases[c]
        N = case.pop(0)
        #print(N, case)
        diff = min_div(case)
        a = 0
        b = max_mult(case)
        for i in case:
            a += int(b//i)
        N = N%a
        #print(N, b)
        if N > 0:
            time = 0
            position = 0
            result = 0
            flag = True
            while flag:
                for i in range(len(case)):
                    if time%case[i] == 0:
                        position += 1
                        if position == N:
                            result = i
                            flag = False
                            break
                time += diff
            print("Case #{}: {}".format(c+1, result+1), file=f_out)
        else:
            result = len(case)
            print("Case #{}: {}".format(c+1, result), file=f_out)
    f_out.close()

def main():
    cases, f_out = reader('B-large-practice.in')
    solver(cases, f_out)

main()
#print(max_mult([18,7,21,11,25]))