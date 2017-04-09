import os


def reader(file):
    f_out = file[:-2]+"out"
    if os.path.isfile(f_out):
        with open(f_out, 'w') as f:  # clear the output file
            f.write('')
    with open(file, 'r') as f:
        T = int(f.readline())
        for t in range(T):
            line = f.readline()
            solver(t, line, f_out)


def solver(t, line, f_out):
    print("Solving #{} case.".format(t+1))
    solution = flip(line)
    with open(f_out, 'a') as f:
        f.write("Case #{}: {}\n".format(t + 1, solution))
    print("Case #{} solved.".format(t+1))


def flip(line):
    pancakes, K = parser(line)
    x = 0
    while -1 in pancakes:
        start = pancakes.index(-1)
        for i in range(start, start + K):
            try:
                pancakes[i] *= -1  # flipping
            except IndexError:
                return "IMPOSSIBLE"
        x += 1
    return x


def parser(line):
    pancakes, K = line.split(' ')
    trans = {'+': 1, '-': -1}
    return [trans[v] for v in pancakes], int(K)


def main():
    reader('A-large.in')

main()
