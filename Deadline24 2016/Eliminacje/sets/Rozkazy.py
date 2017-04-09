import time
def reader(plik):
    f = open(plik)
    l_1 = f.readline()                           
    NM = list(eval(l_1.replace(" ",",")))
    N = NM[0]                                           #liczba miast
    M = NM[1]                                           #liczba dróg
    lista = []                                          #połączenia wejściowe
    for i in range(M):                                
        li_2 = f.readline()
        abd = list(eval(li_2.replace(" ",",")))
        lista.append(abd)
    T = int(f.readline())                               #liczba przypadków na mapie
    cases = []
    for i in range(T):
        cases.append({})
        HK = f.readline()
        HK = list(eval(HK.replace(" ",",")))
        H = HK[0]-1                                     #miasto główne
        K = HK[1]                                       #kolejność pozostałych
        li_3 = f.readline()
        order = list(eval(li_3.replace(" ",",")))
        for o in range(len(order)):
            order[o] -= 1
        cases[i]["H"] = H
        cases[i]['order'] = order   
    return N,M,lista,cases

#### NAZWA PLIKU!!!
for i in range(0,1):
    nazwa = 'orders0'+str(i)+'.in'                                   ######### TU WPISZ NAZWĘ PLIKU!!!!!
    print("FILE: {}".format(nazwa))
    N,M,lista,cases = reader(nazwa)                 
    macierz = []
    for i in range(N):
        macierz.append([])
        for j in range(N):
            macierz[i].append(10**6)
    for j in lista:
        if j[2] < macierz[j[0]-1][j[1]-1]:
            macierz[j[0]-1][j[1]-1] = j[2]
            macierz[j[1]-1][j[0]-1] = j[2]

    """for i in macierz:
        print(i)
    print("\n")"""

    def Dixtra(macierz):
        print(time.asctime(time.gmtime()))
        dix = []
        for s in range(N):
            m_d = []
            for i in range(N):
                m_d.append([])
                for j in range(N):
                    m_d[i].append(10**6)
            m_d = [macierz[s]]
            k = 1
            while k < 10**6:
                if k in m_d[0]:  
                    for p in range(len(m_d[0])):
                        if m_d[0][p] == k:
                            m_d.append(macierz[p])
                            for x in range(len(m_d[0])):
                                if m_d[0][x] > m_d[1][x]+k:
                                    m_d[0][x] = m_d[1][x]+k
                            del m_d[1]
                k += 1
            #print(time.asctime(time.gmtime()))
            #print(m_d[0])
            dix.append(m_d[0])
        for i in range(len(dix)):
            dix[i][i] = 0
            #print(dix[i])
        return dix
    #otwórz plik
    nazwa_ans = nazwa[:-2]+'ans'
    ans_file = open(nazwa_ans,'w')

    diks = Dixtra(macierz)
    #print(cases)
    for c in cases:
        H = c['H']
        order = c['order']
        trucks = [H,H,H]
        #print('Trucks: {}'.format(trucks))
        road_sum = 0
        for o in range(len(order)):
            t_dist = []
            for t in range(len(trucks)):
                t_dist.append(diks[trucks[t]][order[o]])
            #print('Odległości: {}'.format(t_dist))
            t_min = t_dist.index(min(t_dist))
            road_sum += min(t_dist)
            #print('Truck {}: {} -> {}, dist:{}'.format(t_min,trucks[t_min],order[o],min(t_dist)))
            trucks[t_min] = order[o]
            #print('Trucks: {}'.format(trucks))
        for t in range(len(trucks)):
            road_sum += diks[trucks[t]][H]
            #print('Truck {}: {} -> {}, dist:{}'.format(t,trucks[t],H,diks[trucks[t]][H]))
            trucks[t] = H     
        #print(road_sum)
        print(road_sum,file = ans_file)

    ans_file.close()
        
    






