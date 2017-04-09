import os
import math


def reader(file):
    f_out = file[:-2] + "out"
    if os.path.isfile(f_out):
        with open(f_out, 'w') as f:  # clear the output file
            f.write('')
    with open(file, 'r') as f:
        T = int(f.readline())
        for t in range(T):
            line = f.readline()
            solver(t, line, f_out)


def solver(t, line, f_out):
    print("Solving case #{}.".format(t + 1))
    n, k = map(int, line.split(' '))
    print("Parameters N: {}, K: {}.".format(n, k))
    _min, _max = logarythmic_approach(n, k)
    with open(f_out, 'a') as f:
        f.write("Case #{}: {} {}\n".format(t+1, _max, _min))
    print("Case #{} solved.".format(t + 1))
    print('*'*10)


def logarythmic_approach(n, k):
    b = int(math.log(k, 2))
    level = 2**b
    c = (n - level + 1)/level
    c_f = math.floor(c)
    c_c = math.ceil(c)
    x = n - (1 + c_f) * level + 1
    sol = c_f if k >= level + x else c_c
    p_sol = sol // 2
    if sol % 2 == 0:
        l, r = p_sol - 1, p_sol
    else:
        l, r = p_sol, p_sol
    return l, r


def decompose_stalls(n):
    """ Deprecated """
    stalls = [[n]]
    count = [1]
    i = 0
    while True:
        level = stalls[i]
        stalls.append([])
        for d in level:
            x = d // 2
            if d % 2 == 0:
                l, r = x - 1, x
            else:
                l, r = x, x
            stalls[i+1].insert(0, r)  # r is greater
            stalls[i+1].append(l)  # l is lower
        count.append(2**(i+1))
        i += 1


def select_best_stall_fast(stalls):
    """ Deprecated """
    max_l = stalls[0]
    index = stalls.index(max_l)
    x = max_l // 2
    if max_l % 2 == 0:
        l, r = x - 1, x
    else:
        l, r = x, x
    stalls.pop(index)
    stalls.insert(index, r)
    stalls.insert(index, l)
    return stalls, l, r


def select_best_stall(stalls):
    """Deprecated"""
    spaces = stalls.split('O')
    max_l = max(map(lambda x: len(x), spaces))
    index = 0
    for i, s in enumerate(spaces):
        if len(s) == max_l:
            index = i
            break
    x = max_l // 2
    if max_l % 2 == 0:
        l, r = x - 1, x
        i = x - 1
    else:
        l, r = x, x
        i = x
    spaces[index] = spaces[index][:i] + 'O' + spaces[index][i+1:]
    return 'O'.join(spaces), l, r


def calc_zero_border(number):
    """ Deprecated """
    if number == 0:
        return 0
    if number == 1:
        return 0
    if number % 2 == 0:
        return calc_zero_border(number/2 - 1) + calc_zero_border(number/2) + 1
    k = int(number/2)
    return calc_zero_border(k) * 2 + 1


def main():
    import time
    a = time.time()
    reader('C-large.in')
    b = time.time()
    print("Cases solved in {}s.".format(b-a))

main()
