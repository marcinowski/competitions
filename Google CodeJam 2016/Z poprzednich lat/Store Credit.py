def reader(plik):
    f = open(plik)
    N = int(f.readline())
    cases = []
    for t in range(N):
        C = int(f.readline())
        I = int(f.readline())
        li_2 = f.readline()
        P_list = list(eval(li_2.replace(" ",",")))
        P_list.insert(0,C)
        cases.append(P_list)
    f_out = plik[:-2] + "out"
    return cases, f_out

def solve(cases, f_out):
    f_out = open(f_out, 'w')
    for case in cases:
        P = case.pop(0)
        for i in range(len(case)):
            flag = False
            temp = case[i+1:]
            for j in range(len(temp)):
                if case[i]+temp[j] == P:
                    print("Case #{}: {} {}".format(cases.index(case)+1,i+1,i+j+2), file = f_out)
                    flag = True
                    break
            if flag:
                break
    f_out.close()


def main():
    cases, f_out = reader("Store Credit A-large-practice.in")
    solve(cases, f_out)

main()
        

