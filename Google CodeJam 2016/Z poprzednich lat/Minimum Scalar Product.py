def reader(plik):
    f = open(plik)
    N = int(f.readline())
    cases = []
    for t in range(N):
        case = []
        #C - rząd wektora
        C = f.readline()
        #wektor 1
        vect_1 = f.readline()
        vect_1 = str_to_list(vect_1)
        case.append(vect_1)
        #wektor 2
        vect_2 = f.readline()
        vect_2 = str_to_list(vect_2)
        case.append(vect_2)
        cases.append(case)
    f_out = plik[:-2] + "out"
    return cases, f_out

def str_to_list(string):
    result = []
    i = 0
    temp = ""
    while i<len(string):
        if string[i] == " ":
            result.append(int(temp))
            temp = ""
        elif string[i] == "\n":
            result.append(int(temp))
            break
        else:
            temp += string[i]
        i += 1
    return result   

def scalar(vect_1,vect_2):
    result = 0
    for i in range(len(vect_1)):
        result += vect_1[i]*vect_2[i]
    return result

def solve(cases, f_out):
    f_out = open(f_out,'w')
    for i in range(len(cases)):
        vect_1 = cases[i][0]
        vect_2 = cases[i][1]
        vect_1.sort()
        vect_2.sort()
        vect_1 = vect_1[::-1]
        result = scalar(vect_1,vect_2)
        print("Case #{}: {}".format(i+1,result), file = f_out)
    f_out.close()
        
def main():
    cases, f_out = reader("A-large-practice.in")
    solve(cases, f_out)

main()
