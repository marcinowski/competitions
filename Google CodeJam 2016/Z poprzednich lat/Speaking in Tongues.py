def reader(file):
    f = open(file,'r')
    f_out = file[:-2] + "out"
    T = int(f.readline())
    cases = []
    for t in range(T):
        line_1 = f.readline()
        cases.append(line_1)
    f.close()
    return cases, f_out

def solver(cases, f_out):
    keys = ["eokidsnbhxmlgvprtwfc", "ay","ju","qz"]
    for k in range(len(keys)):
        keys[k] = keys[k][::-1]
    f_out = open(f_out,'w')
    for i in range(len(cases)):
        case = cases[i]
        if case[-1] == "\n":
            case = case[:-1]
        for l in range(len(case)):
            letter = case[l]
            for key in keys:
                if letter in key:
                    ind = key.index(letter)
                    case = case[:l]+key[ind-1]+case[l+1:]
        print("Case #{}: {}".format(i+1, case), file=f_out)

def main():
    cases, f_out = reader("A-small-practice.in")
    solver(cases,f_out)

main()
        
