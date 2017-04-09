def mean(list1,list2):
    res = [(list1[i] - list2[i])**2 for i in range(len(list1))]
    avg = int(sum(res)/len(res))
    return avg


def main(it = 128):
    for a in range(0,11):
        if a<10:
            plik = "wez0"+str(a)+".in"
        else:
            plik = "wez10.in"
        f = open(plik,'r')
        text = f.readline()
        text1 = [ord(i) for i in text]                  #lista z wartości ASCII liter z tekstu
        if text[-1] == "\n":
            text1.pop(-1)                               #usuwa znak końca linii
        comp_0 = 10**5                                  #wstępna granica punktacji, im mniej tym lepiej
        for i in range(it):                             #i jako seed ma być z zakresu 0<i<2**31
            text2 = []                                  #tworzenie nowej listy z losowymi wartościami
            seed = i                                    #i jako seed
            for j in text1:                             #dla każdej litery z listy text1
                x_n = (1103515245*seed+12345)%2**31     #twórz losową liczbę
                text2.append(x_n%128)                   #dodaj do text2 liczbę ASCII
                seed = x_n                              #nowy seed
            comp = mean(text1,text2)                    #dla text2 i text2 oblicz średnią
            if comp < comp_0:                           #jeśli obliczona średnia jest lepsza od wstępnej 
                comp_0 = comp                           #zastąp 
                seed_1 = i                              #przypisz najlepszy seed
                """print("Zmiana", seed_1, comp)
                print(text2,len(text2))                 #wypisz
                text2 = [chr(i) for i in text2]
                print(''.join(text2))"""
        plik_out = plik[:-2]+"out"
        f = open(plik_out,'w')
        print(comp_0)
        print(seed_1, file = f)

main()
            
            
        
