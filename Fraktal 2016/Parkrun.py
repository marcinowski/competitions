N = int(input())
best = []
f_max = 3600
for n in range(N):
    case = input().strip().split(' ')
    t = case[2].split(':')
    f = int(t[0])*60 + int(t[1])
    if f == f_max:
        best.append([case[0], case[1], case[2]])
    elif f < f_max:
        best = []
        best.append([case[0], case[1], case[2]])
        f_max = f
    
for k in best:
    for el in k:
        print(el, end = ' ')
    print('')
