def reader(plik):
    f = open(plik)
    line_1 = f.readline()
    NDL = list(eval(line_1.replace(" ",",")))
    L = NDL[0]
    D = NDL[1]
    N = NDL[2]
    words = []
    for t in range(D):
        line = f.readline()
        words.append(line[:-1])
    cases = []
    for t in range(N):
        line = f.readline()
        cases.append(line[:-1])        
    f_out = plik[:-2] + "out"
    return cases, words, f_out

def solve(cases, words, f_out):
    temp_list = []
    result = [0 for case in cases]
    case_list = []
    for case in cases:
        case_temp = []
        i = 0
        while i<len(case):
            if case[i] == "(":
                i += 1
                a = ""
                while case[i] != ")":
                    a += case[i]
                    i += 1
                case_temp.append(a)
            else:
                case_temp.append(case[i])
            i += 1
        case_list.append(case_temp)
    for case in case_list:
        for word in words:
            for i in range(len(word)):
                if word[i] in case[i]:
                    if i == len(word) - 1:
                        result[case_list.index(case)] += 1
                else: break
    f_out = open(f_out, 'w')
    for i in range(len(result)):
        print("Case #{}: {}".format(i+1, result[i]), file = f_out)
    f_out.close()

def main():
    cases, words, f_out = reader("A-large-practice.in")
    solve(cases, words, f_out)

main()

        


