T9 = [[" "],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]

def reader(plik):
    f = open(plik)
    N = int(f.readline())
    cases = []
    for t in range(N):
        C = f.readline()
        C = C[:-1]
        if len(C) > 0:
            cases.append(C)
    f_out = plik[:-2] + "out"
    return cases, f_out

def solve(cases, f_out):
    f_out = open(f_out, 'w')
    for case in cases:
        case_str = ""
        for letter in case:
            for button in T9:
                if letter in button:
                    clicks = button.index(letter)+1
                    if len(case_str)>0:
                        if case_str[-1] == str(T9.index(button)):
                            case_str += " "
                    case_str += str(T9.index(button))*clicks
        print("Case #{}: {}".format(cases.index(case)+1, case_str), file=f_out)

def main():
    cases, f_out = reader("C-large-practice.in")
    solve(cases, f_out)    

main()

                    
