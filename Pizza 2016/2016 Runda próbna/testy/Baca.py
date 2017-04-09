from decimal import Decimal

for i in range(1,11):
    if len(str(i))==1:
        plik = 'bac0' + str(i) + '.in'
    else:
        plik = 'bac' + str(i) + '.in'
    nogi = open(plik,'r')
    N = int(nogi.read())
    nogi.close()
    #print(N)
    L = N/4
    #print(L)
    plik = plik[:-2]
    plik += ("out")
    print(plik)
    rezultat = open(plik,'w')
    print(L,file = rezultat)
