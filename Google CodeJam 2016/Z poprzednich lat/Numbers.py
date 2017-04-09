def reader(file):
    f = open(file)
    f_out = file[:-2] + 'out'
    T = int(f.readline())
    cases = []
    for t in range(T):
        case = int(f.readline())
        cases.append(case)
    return cases, f_out

def solve(cases, f_out):
    f_out = open(f_out,'w')
    for i in range(len(cases)):
        case = cases[i]
        print(case)
        result = (3 + 5**0.5)**case
        result = int(result//1)
        str_result = str(result)[-3:]
        if len(str_result) < 3:
            a = 3 - len(str_result)
            str_result = '0'*a + str_result
        print('Case #{}: {}'.format(i+1,str_result), file = f_out)
    f_out.close()
    
def main():
    cases, f_out = reader('C-small-practice.in')
    solve(cases,f_out)

main()
