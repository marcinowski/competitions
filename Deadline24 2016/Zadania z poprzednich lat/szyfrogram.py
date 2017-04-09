C = 10
M = 10
x = [2,3,4,10,1]
a = [1,1]
for i in range(max(x)):
    a.append(a[-2]+C*a[-1])
s = []
for i in range(len(a)):
    s.append(sum(a[0:i+1]))
print(a)
print(x)
print(s)
x_s = [(s[a-1])%M for a in x]
print(x_s)

    
