def reader(file):
    f_out = file[:-2]+'out'
    f = open(file, 'r')
    T = int(f.readline())
    cases = []
    for t in range(T):
        N = int(f.readline())
        cases.append(N)
    return cases, f_out

def counter(N):
    i = 0
    while N>0:
        order = len(str(N))
        a = N%10
        if a == 0:
            a = 10
        i += a - 1
        N -= a - 1
        N_2 = int(str(N)[::-1])
        if N_2 >= N:
            b = 0
            for j in range(order-1):
                b += 9*10**j
            i += N - b
            N = b
        else:
            i += 1
            N = N_2
    return i

def solver(cases, f_out):
    f_out = open(f_out,'w')
    for c in range(len(cases)):
        print(c)
        case = cases[c]
        result = counter(case)
        print("Case #{}: {}".format(c+1, result), file=f_out)
    f_out.close()

def main():
    cases, f_out = reader('A-small-practice.in')
    solver(cases, f_out)

main()
