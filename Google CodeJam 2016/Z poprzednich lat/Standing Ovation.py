def reader(file):
    f = open(file)
    f_out = file[:-2] + "out"
    T = int(f.readline())
    cases = []
    for t in range(T):
        line = f.readline()
        sp_index = line.index(" ")
        if line[-1] == "\n":
            case = line[sp_index+1:-1]
        else:
            case = line[sp_index+1:]
        cases.append(case)
    return cases, f_out

def solver(cases, f_out):
    f_out = open(f_out,'w')
    for c in range(len(cases)):
        case = cases[c]
        c_sum = 0
        needed = 0
        for i in range(len(case)):
            if c_sum >= i:
                c_sum += int(case[i])
            else:
                needed += i - c_sum
                c_sum += i - c_sum
                c_sum += int(case[i])
        print("Case #{}: {}".format(c+1, needed), file=f_out)

def main():
    cases, f_out = reader("A-large-practice.in")
    solver(cases, f_out)

main()
        
