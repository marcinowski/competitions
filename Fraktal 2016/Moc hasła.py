N = int(input())
for n in range(N):
    case = input()
    if len(case) >= 8:
        asc = []
        for k in case:
            asc.append(ord(k))
        special = 0
        numbers = 0
        small = 0
        capital = 0
        for i in asc:
            if (32 <= i <= 126):
                if 48 <= i <= 57:
                    numbers += 1
                elif 65 <= i <= 90:
                    capital += 1
                elif 97 <= i <= 122:
                    small += 1
                else:
                    special += 1
        if special*numbers*capital*small > 0:
                print(case)
