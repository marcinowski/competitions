import os


def reader(file):
    f_out = file[:-2] + "out"
    if os.path.isfile(f_out):
        with open(f_out, 'w') as f:  # clear the output file
            f.write('')
    with open(file, 'r') as f:
        T = int(f.readline())
        for t in range(T):
            N, M = map(int, f.readline().split(' '))
            scene = generate_scene(N)
            for _ in range(M):
                sign, x, y = f.readline().strip().split(' ')
                scene[int(x) - 1][int(y) - 1] = sign
            solver(t, scene, f_out)


def generate_scene(n):
    return [['.'] * n for _ in range(n)]


def solver(t, scene, f_out):
    print("Solving #{} case.".format(t + 1))
    points, models, positions = Scene(scene).solve()
    with open(f_out, 'a') as f:
        f.write("Case #{}: {} {}\n".format(t + 1, points, models))
        for p in positions:
            f.write(p + '\n')
    print("Case #{} solved.".format(t + 1))
    print("*" * 20)


class RulesViolation(Exception):
    """"""


class Scene(object):
    def __init__(self, scene):
        self.scene = scene
        self.N = len(scene)
        print("N {}".format(self.N))

    def solve(self):
        positions = []
        for i in range(self.N):
            for j in range(self.N):
                curr_sign = self.scene[i][j]
                if curr_sign == '.':
                    s = self.try_insertion(i, j, curr_sign, ['o', '+', 'x'])
                elif curr_sign in ['+', 'x']:
                    s = self.try_insertion(i, j, curr_sign, ['o'])
                else:
                    continue
                if s:
                    positions.append('{} {} {}'.format(s, i+1, j+1))
        points = self.calculate_points()
        return points, len(positions), positions

    def calculate_points(self):
        points = 0
        for s in self.scene:
            points += s.count('+')
            points += s.count('x')
            points += s.count('o') * 2
        return points

    def print(self):
        for p in self.scene:
            print(p)

    def try_insertion(self, i, j, curr, sign_set):
        for s in sign_set:
            try:
                self.scene[i][j] = s
                self._check_rules_for_point(i, j)
            except RulesViolation:
                self.scene[i][j] = curr
                continue
            else:
                return s

    def _check_rules_for_point(self, i, j):
        self._check_row(i)
        self._check_column(j)
        self._check_p_diagonal(i, j)
        self._check_n_diagonal(i, j)

    def _check_row(self, i):
        self._check_plus(self.scene[i], '+', self.N, 'row {}'.format(i))

    def _check_column(self, i):
        c = [s[i] for s in self.scene]
        self._check_plus(c, '+', self.N, 'column {}'.format(i))

    def _check_p_diagonal(self, i, j):
        sum = i + j
        opts = [(a, sum - a) for a in range(self.N) if a < self.N and sum - a < self.N]
        c = [self.scene[m][n] for m, n in opts]
        if c:
            self._check_plus(c, 'x', len(c), 'positive diagonal')

    def _check_n_diagonal(self, i, j):
        i, j = (i, j) if i > j else (j, i)
        sum = i - j
        opts = [(a, a - sum) for a in range(self.N) if a < self.N and a - sum < self.N]
        c = [self.scene[m][n] for m, n in opts]
        if c:
            self._check_plus(c, 'x', len(c), 'negative diagonal')

    @staticmethod
    def _check_plus(a, sign, n, message):
        dots = a.count('.')
        if dots < n - 1:
            if a.count(sign) < n - dots - 1:
                raise RulesViolation('Too few {} characters in {}.'.format(sign, message))


def main():
    import time
    a = time.time()
    reader('D-small.in')
    b = time.time()
    print("Cases solved in {}s.".format(b-a))

main()
