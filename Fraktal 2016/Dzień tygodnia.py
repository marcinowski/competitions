days = ['Pn', 'Wt', 'Sr', 'Cz', 'Pt', 'So', 'Nd']
D = int(input())
for d in range(D):
	case = input().strip().split(' ')
	a = days.index(case[0])
	b = int(case[1])
	result = (a+b)%7
	print(days[result])
