def reader(file):
    f_out = file[:-2]+'out'
    f = open(file, 'r')
    T = int(f.readline())
    cases = []
    for t in range(T):
        N = int(f.readline())
        case = f.readline().strip().split(' ')
        for c in range(len(case)):
            case[c] = int(case[c])
        cases.append(case)
    return cases, f_out

def solver(cases, f_out):
    f_out = open(f_out,'w')
    for c in range(len(cases)):
        case = cases[c]
        temp = [case[i - 1] - case[i] for i in range(1, len(case)) if case[i - 1] > case[i]]
        result_1 = sum(temp)
        try:
            max_1 = max(temp)
        except ValueError:
            max_1 = 0
        result_2 = 0
        for i in range(len(case)-1):
            if case[i] <= max_1:
                result_2 += case[i]
            else:
                result_2 += max_1
        print("Case #{}: {} {}".format(c + 1, result_1, result_2), file=f_out)
    f_out.close()

def main():
    cases, f_out = reader("A-large-practice.in")
    solver(cases, f_out)

main()