for i in range(1,6):
    if i<10:
        plik = 'probe0' + str(i) + '.in'
    else:
        plik = 'probe' + str(i) + '.in'
    kl = open(plik)
    L = int(kl.readline())
    print(L)
    plik_o = plik[:-2]+"ans"
    if L>0:
        a = '1'
    elif L<0:
        a = '-1'
    elif L == 0:
        a = '0'
    plik_o = open(plik_o,'w')
    print(a,file = plik_o)
    plik_o.close()
    
