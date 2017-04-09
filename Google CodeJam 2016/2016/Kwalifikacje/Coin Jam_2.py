length = 32
no_of_coins = 500
start = 2**(length-1) + 1
diff = 2**(length-1) - 2**(length-2)

# def reader(file):
#     f = open(file,'r')
#     f_out = file[:-2]+'out'
#     cases = []
#     T = int(f.readline())
#     for t in range(T):
#         NJ = f.readline()
#         NJ_list = NJ.split(' ')
#         cases.append(NJ_list)
#     return cases, f_out

def test_prime(N):
    """returns True if N is prime"""
    limit = int(N**0.5)
    for i in range(2,4):
        if N%i == 0:
            return i
    for i in range(1,int(limit/6)):
        for j in range(-1,1):
            div = 6*i+j
            if N%div == 0:
                return div
    return 1

def get_divisor(N):
    limit = int(N**0.5)+1
    for i in range(2,limit,2):
        if N%i == 0:
            return i

def base_translate(string):
    """string must be a binary form"""
    result = []
    string = string[2:]
    for i in range(2,11):
        base_i = 0
        for s in range(0,len(string)):
            a = string[-s-1]
            base_i += int(a)*(i**s)
        result.append(base_i)
    return result

def bin_generator():
    result = []
    b_0 = bin(start)
    result.append(b_0)
    for i in range(diff):
        b_iter = bin(int(result[-1],base=2)+2)
        yield b_iter
        result.append(b_iter)

def main():
    num_iter = bin_generator()
    result = []
    while len(result) < no_of_coins:
        number = next(num_iter)
        bases = base_translate(number)
        divs = []
        flag = True
        for i in bases:
            temp = test_prime(i)
            if temp == 1:
                flag = False
                break
            else:
                divs.append(temp)
        if flag:    
            result.append([number[2:], divs])
            print(len(result))
    return result
    
def printer(result):
    file = 'C-large_2.out'
    f_out = open(file,'w')
    print("Case #1:", file = f_out)
    for i in result:
        string = i[0] + ' '
        for j in i[1]:
            string += str(j)
            string += ' '
        print(string, file = f_out)
    f_out.close()

list = main()
printer(list)

# a=base_translate('0b10001')
# print(a)
