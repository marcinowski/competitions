def reader(file):
    f = open(file,'r')
    f_out = file[:-2]+"out"
    T = int(f.readline())
    cases = []
    for t in range(T):
        line = f.readline().strip()
        cases.append(line)
    return cases, f_out

def solver(cases, f_out):
    f_out = open(f_out,'w')
    for c in range(len(cases)):
        case = cases[c]
        names = ["SIX", "SEVEN", "FIVE", "EIGHT", "FOUR", "ZERO", "NINE", "TWO", "THREE", "ONE"]
        nums = ['6', '7', '5', '8', '4', '0', '9', '2', '3', '1']
        number = ''
        letters = ['X', 'S', 'V', 'G', 'F', 'Z', 'N', 'W', 'T', 'E']
        while len(case) > 0:
            for a in letters:
                k = letters.index(a)
                if a in case:
                    number += nums[k]
                    for j in names[k]:
                        case = case.replace(j, '', 1)
                        print(case)
                    break
        print(number)

def main():
    cases, f_out = reader('C-test.in')
    solver(cases, f_out)

main()


