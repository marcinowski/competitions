def reader(file):
    f = open(file)
    f_out = file[:-2] + "out"
    N = int(f.readline())
    cases = []
    for n in range(N):
        cases.append(f.readline())
        if "\n" in cases[-1]:
            cases[-1] = cases[-1][:-1]
    return cases, f_out

def solver(cases, f_out):
    f_out = open(f_out,'w')
    base = "welcome to code jam"
    #print(base)
    print(len(cases))
    for i in range(len(cases)):
        print(i)
        case = cases[i]
        counter = recurrence(case, base, 0, 0, counter=0)
        result = str(counter)[-4:]
        if len(result) < 4:
            mult = 4 - len(result)
            result = '0'*mult + result
        print("Case #{}: {}".format(i+1,result), file = f_out)
    f_out.close()

def recurrence(case, base, c_ind, b_ind, counter):
    #print(c_ind, b_ind, counter)
    if b_ind == len(base):
        counter += 1
        #print(counter, type(counter))
        return counter
    elif c_ind < len(case):
        temp_case = case[c_ind:]
        indexes = [c_ind + i for i in range(len(temp_case)) if temp_case[i] == base[b_ind]]
        #print(base[b_ind], indexes)
        if len(indexes) == 0:
            return counter
        else:
            for ind in indexes:
                counter = recurrence(case, base, ind, b_ind+1, counter)
            return counter
    else:
        return counter

def main():
    cases, f_out = reader("C-large-practice.in")
    solver(cases, f_out)

main()
