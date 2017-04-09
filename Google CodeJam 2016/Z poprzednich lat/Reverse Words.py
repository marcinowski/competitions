def reader(plik):
    f = open(plik)
    N = int(f.readline())
    cases = []
    for t in range(N):
        temp = []
        C = f.readline()
        s = ""
        i = 0
        while i <= len(C):
            if C[i] == "\n":
                temp.append(s)
                break
            elif C[i] == " ":
                temp.append(s)
                s = ""
            else:
                s += C[i]
            i += 1
        cases.append(temp)
    f_out = plik[:-2] + "out"
    return cases, f_out

def solve(cases, f_out):
    f_out = open(f_out, 'w')
    for case in cases:
        temp = case[::-1]
        print("Case #{}: ".format(cases.index(case)+1), end = '', file = f_out)
        for i in temp:
            print(i, sep='', end = ' ', file = f_out)
        print("\n", file = f_out)

def main():
    cases, f_out = reader("B-large-practice.in")
    solve(cases, f_out)

main()
