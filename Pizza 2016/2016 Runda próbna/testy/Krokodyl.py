for i in range(1,11):
    if i<10:
        plik = 'kro0' + str(i) + '.in'
    else:
        plik = 'kro' + str(i) + '.in'
    kl = open(plik)
    L = int(kl.readline())-1
    plik = plik[:-2]+"out"
    result = open(plik,'w')
    print(L)
    print("            .-._   _ _ "+L*"_ _ "+"_ _ _ _ _ _        ",sep = '\n', file = result)     
    print(" .-''-.__.-'00  '-' ' '"+L*" ' '"+" ' ' ' ' ' '-.     ",sep = '\n', file = result)   
    print(" '.___ '    .   .--_'-'"+L*" '-'"+" '-' '-' _'-' '._  ",sep = '\n', file = result)
    print("  V: V 'vv-'   '_   '. "+L*"    "+"      .'  _..' '.'.",sep = '\n', file = result)
    print("    '=.____.=_.--'   :_"+L*"._._"+"._._._:_   '.   : :",sep = '\n', file = result)
    print("           (((____.-'  "+L*"    "+"      '-.  /   : : ",sep = '\n', file = result)
    print(" snd                   "+L*"    "+"      (((-'\ .' /  ",sep = '\n', file = result)
    print("                       "+L*"    "+"    _____..'  .'   ",sep = '\n', file = result)
    print("                       "+L*"    "+"   '-._____.-'     ",sep = '\n', file = result)
