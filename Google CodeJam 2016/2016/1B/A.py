names = ["ONE", "TWO", "THREE", "FOUR", "FIVE", 'SIX', "SEVEN", "EIGHT", "NINE", "ZERO"]
def reader(file):
    f = open(file,'r')
    f_out = file[:-2]+"out"
    T = int(f.readline())
    cases = []
    for t in range(T):
        case = []
        K = int(f.readline())
        for k in range(K):
            line = f.readline().strip().split(" ")
            case.append(line)
        cases.append(case)
    return cases, f_out

def solver(cases, f_out):
    f_out = open(f_out,'w')
    for c in range(len(cases)):
        case = cases[c]
        first = []
        second = []
        repeats = []
        result = 0
        for i in range(len(case)):
            first.append(case[i][0])
            second.append(case[i][0])
        for j in range(len(first)):
            a = first.count(first[j])
            if a > 1:
                repeats.append(case[j])
        for j in range(len(second)):
            a = second.count(second[j])
            if a > 1:
                repeats.append(case[j])
        for r in range(len(repeats)-1):
            for j in range(r+1,len(repeats)):
                if repeats[r][0] == repeats[j][0]:
                    if repeats[r][1] == repeats[j][1]:
                        result += 1
                elif repeats[r][1] == repeats[j][1]:
                    if repeats[r][0] == repeats[j][0]:
                        result += 1
        print(result//2)

def main():
    cases, f_out = reader('A-test.in')
    solver(cases, f_out)

main()







