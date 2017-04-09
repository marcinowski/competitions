def reader(plik):
    f = open(plik)
    T = int(f.readline())                                   #liczba działek
    cases = []
    for t in range(T):
        cases.append({})
        l_1 = f.readline()
        NK = list(eval(l_1.replace(" ",",")))
        N = NK[0]                                           #liczba punktów FP
        K = NK[1]                                           #liczba max wyłączonych FP
        lista = []                                          #połączenia wejściowe
        for i in range(N):                                  
            li_2 = f.readline()
            lista.append({})
            cxy = list(eval(li_2.replace(" ",",")))
            lista[i]["id"] = cxy[0]
            lista[i]["yx"] = cxy[1:]            
        cases[-1] = {"N":N, "K": K, 'FPs': lista}
    return cases

def sort(xy,coordinates):
    """xy - string 'x' or 'y', for an axis you want to sort by"""
    coords = coordinates[:]
    if xy == "x":
        k = 1
    else:
        k = 0
    flag = True
    while flag:
        flag = False
        for i in range(1,len(coords)-1):
            if coords[i][k]>coords[i+1][k]:
                coords[i],coords[i+1] = coords[i+1],coords[i]
                flag = True
    return coords

def Jarvis(coords):
    coords_y = sort('y',coords)
    coords_x = sort('x',coords)
    pass  

def main():
    cases = reader('rancho00.in')
    for case in cases:
        print("CASE: {}".format(cases.index(case)))
        FPs = case["FPs"]
        N = case["N"]
        K = case["K"]
        minx,miny,maxx,maxy = 10**4,10**4,0,0
        for fp in FPs:
            if fp['yx'][0] < miny:
                miny = fp['yx'][0]
            if fp['yx'][1] < minx:
                minx = fp['yx'][1]
            if fp['yx'][0] > maxy:
                maxy = fp['yx'][0]
            if fp['yx'][1] > maxx:
                maxx = fp['yx'][1]
            #print('{}: {}'.format(fp["id"],fp["xy"]))
        rancho = []
        for y in range(miny,maxy+1):
            rancho.append([])
            for x in range(minx,maxx+1):
                rancho[-1].append(0)
        for fp in FPs:
            fp['yx'][0] -= miny
            fp['yx'][1] -= minx
            #print('{}: {}'.format(fp["id"],fp["xy"]))
            rancho[fp['yx'][0]][fp['yx'][1]] = fp['id']
        coords = [f["yx"] for f in FPs]
        for i in rancho:
            for j in i:
                print(j,end="")
            print("")
        ##MAX
        max_rancho = []
        for x in range(len(rancho)):
            max_rancho.append([])
            for y in range(len(rancho[x])):
                pass
        ##MIN
        min_rancho = []
                    
#main()
    
