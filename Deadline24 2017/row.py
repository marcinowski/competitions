def reader(file):
    f = open(file, 'r')
    f_out = file[:-2]+"out"
    t = int(f.readline())
    cases = []
    for _t in range(t):
        _cases = []
        t = int(f.readline())
        for i in range(2):
            line = list(map(int, f.readline().strip().split(' ')))
            _cases.append(line)
        cases.append(_cases)
    return cases, f_out


def case_solver(case, f):
    result = []
    temp = []
    for i, _i in enumerate(case[0]):
        temp.append(_i)
        for j, _j in enumerate(case[1]):
            if i < j:
                temp.append(_j)
                break
        result.append(temp)
        temp = []
    print(result)


def solver(cases, f_out):
    with open(f_out, 'w') as f_out:
        for c in cases:
            case_solver(c, f_out)


def main():
    # for i in range(10):
    #     cases, f_out = reader('row0{}.in'.format(i))
    #     solver(cases, f_out)
    cases, f_out = reader('row00.in')
    solver(cases, f_out)

main()
