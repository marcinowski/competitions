def reader(file):
    f = open(file)
    f_out = file[:-2] + "out"
    T = int(f.readline())
    cases = []
    for t in range(T):
        case_map = []
        HW = f.readline()
        HW = list(eval(HW.replace(" ", ",")))
        H = HW[0]
        W = HW[1]
        for h in range(H):
            w = f.readline() 
            try:
                case_map.append(list(eval(w.replace(" ", ","))))
            except TypeError:
                case_map.append([int(w[:-1])])
        cases.append(case_map)
    return cases, f_out

def solver(cases, f_out):
    f_out = open(f_out, 'w')
    for case in cases:
        """for i in case:
            print(i)
        print("\n")"""
        surr = [[-1,0],[0,-1],[0,1],[1,0]]
        drain_dir_map = [[0 for w in y] for y in case]
        rose = ["N", "W", "E", "S"]
        drains = []
        for y in range(len(case)):
            for x in range(len(case[y])):
                cell_alt = case[y][x]
                cell_surr = []
                for drct in surr:
                    if (len(case) > y+drct[0] >= 0) and (len(case[y]) > x+drct[1] >= 0):
                        cell_surr.append(case[y+drct[0]][x+drct[1]])
                    else:
                        cell_surr.append(cell_alt)
                cell_min = min(cell_surr)
                cell_lower = cell_surr.count(cell_min)
                if cell_min < cell_alt:
                    if cell_lower == 1:
                        drain_dir_map[y][x] = rose[cell_surr.index(cell_min)]
                    if cell_lower > 1:
                        temp_rose = [rose[i] for i in range(len(cell_surr)) if cell_surr[i] == cell_min]
                        drain_dir_map[y][x] = temp_rose[0]                        
                else:
                    drain_dir_map[y][x] = "D"
                    drains.append([y,x])
        """for a in drain_dir_map:
            print(a)
        print("\n")"""
        rose_rev = rose[::-1]
        drain_map = [['0' for w in y] for y in case]
        letters = []
        for drain in drains:
            letter = chr(97+drains.index(drain))
            letters.append(letter)
            drain_map[drain[0]][drain[1]] = letter
            flag_drain = True
            while flag_drain:
                flag_drain = False
                for y in range(len(drain_map)):
                    for x in range(len(drain_map[y])):
                        if drain_map[y][x] == letter:
                            for drct in surr:
                                if (len(drain_map) > y+drct[0] >= 0) and (len(drain_map[y]) > x+drct[1] >= 0):
                                    cell_n = drain_dir_map[y+drct[0]][x+drct[1]]
                                    if cell_n == rose_rev[surr.index(drct)]:
                                        if drain_map[y+drct[0]][x+drct[1]] != letter:
                                            drain_map[y+drct[0]][x+drct[1]] = letter
                                            flag_drain = True
        """for a in drain_map:
            print(a)"""
        drain_letters = []
        for y in range(len(drain_map)):
            for x in range(len(drain_map[y])):
                if drain_map[y][x] not in drain_letters:
                    drain_letters.append(drain_map[y][x])
        for y in range(len(drain_map)):
            for x in range(len(drain_map[y])):
                cur_let = drain_map[y][x]
                ind = drain_letters.index(cur_let)
                drain_map[y][x] = letters[ind]      
    
        print("Case #{}:".format(cases.index(case)+1), file = f_out)
        for line in drain_map:
            for cell in line:
                print(cell, end = ' ', file = f_out)
            print("", file = f_out)
            
    f_out.close()         

def main():
    cases, f_out = reader("B-large-practice.in")
    solver(cases, f_out)

main()
            
