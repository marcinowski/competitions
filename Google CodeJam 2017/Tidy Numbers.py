import os


def reader(file):
    f_out = file[:-2] + "out"
    if os.path.isfile(f_out):
        with open(f_out, 'w') as f:  # clear the output file
            f.write('')
    with open(file, 'r') as f:
        T = int(f.readline())
        for t in range(T):
            line = f.readline().strip()
            solver(t, line, f_out)


def solver(t, line, f_out):
    print("Solving #{} case.".format(t + 1))
    solution = two_numbers_solve(line)
    with open(f_out, 'a') as f:
        f.write("Case #{}: {}\n".format(t + 1, solution))
    print("Case #{} solved.".format(t + 1))
    print("*" * 20)


def number_solve(n):
    while not is_number_tidy(n):
        n -= n % 10 + 1
    return n


def is_number_tidy(number):
    number = str(number)
    """ number is type: string """
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            return False
    return True


def two_numbers_solve(n):
    """ n is string """
    print("Parsing {}".format(n))
    n_b = n[::-1]  # let's go backwards
    for i in range(len(n_b)-1):
        c = n_b[i:i+2]
        if c[0] < c[1]:
            print("Error detected: {} (index {})".format(c[::-1], i))
            x = int(c[::-1])
            x -= x % 10 + 1
            replacement = str(x)[::-1]
            if len(replacement) == 1:
                replacement += '0'
            n_b = n_b.replace(c, replacement, 1)
            if i > 0:
                n_b = n_b.replace(n_b[:i], '9'*i, 1)
            print("Error replaced with {}. New number {}".format(replacement[::-1], n_b[::-1]))
    solution = n_b[::-1]
    if solution.startswith('0'):
        solution = solution[1:]
    print("Final form: {}".format(solution))
    return solution


def main():
    reader('B-large.in')

main()
