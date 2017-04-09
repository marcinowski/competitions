def reader(file):
    f = open(file)
    f_out = file[:-2] + "out"
    T = int(f.readline())
    cases = []
    for t in range(T):
        line = list(eval(f.readline().replace(" ",",")))
        cases.append(line)
    return cases, f_out

def solver(cases, f_out):
    f_out = open(f_out,'w')
    for c in range(len(cases)):
        print(c)
        case = cases[c]
        case_res = recycled(case)
        print("Case #{}: {}".format(c+1, case_res), file = f_out)

def recycled(case):
    down_limit = case[0]
    up_limit = case[1]
    pool = list(range(down_limit,up_limit+1))
    result = 0
    control = []
    for num in range(down_limit, up_limit+1):
        if num in pool:
            pool.remove(num)
            num_str = str(num)
            for n in range(1,len(num_str)):
                rec_num = num_str[-n:]+num_str[:-n]
                if rec_num[0] != '0':
                    rec_num_int = int(rec_num)
                    if rec_num_int > num and rec_num_int <= up_limit:
                        #print(num, rec_num_int)
                        test = [num,rec_num_int]
                        if test not in control:
                            control.append(test)
                            result += 1                   
    return result

def main():
    cases, f_out = reader("C-large-practice.in")
    solver(cases, f_out)

main()
