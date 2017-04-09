C = 6
Q = 20
m_x = 9
m_y = 9
ID = [[1,7,13,0,10,7,0],
      [2,5,5,3,9,2,2],
      [3,14,17,1,25,4,1],
      [4,19,22,3,24,1,3],
      [5,15,6,40,45,2,5]]

ID_d = ['x','y','b','e','d','s']

ID_dict = {}
for i in ID:
    temp = {}
    for j in range(1,len(ID_d)):
        temp[ID_d[j]] = i[j]
    ID_dict[str(i[0])] = temp

for i in ID_dict:
    print(i)

k = 1
Trucks = {}
while len(ID_dict) > 0:
    Trucks[str(k)] = {'x':m_x,'y':m_y, 'Q':Q, 't':0}
    while Q>0:
        dest = {}
        truck = Trucks[str(k)]
        for key in ID_dict:
            for i in key:
                d_i = str(i)
                dest[d_i] = {'dist':0,'t_max':0,'Q>d':0}
                dest[d_i]['dist'] = abs(truck['x']-i['x'])+abs(truck['y']-i['y'])
                dest[d_i]['t_left'] = i['e']-dest[d_i]['dist']
                dest[d_i]['Q>d'] = bool(truck['Q'] > i['d'])
        t_min = {a:dest[a]['t_left'] for a in dest}
        dests = [len(ID_dict)]
        for i in t_min:
            if t_min[i] < t_min[str(dests[0])]:
                dests.clear()
                dests.append(i)
            elif t_min[i] == t_min[str(dests[0])]:
                if i != str(dests[0]):
                    dests.append(i)
        print(dests)
        while len(dests) != 1:
            if ID_dict[int(dests[0])]['b'] < ID_dict[int(dests[1])]['b']:
                del dests[1]
            elif ID_dict[int(dests[0])]['b'] > ID_dict[int(dests[1])]['b']:
                del dests[0]
            else:
                if ID_dict[int(dests[0])]['d'] < ID_dict[int(dests[1])]['d']:
                   del dests[1]
                elif ID_dict[int(dests[0])]['d'] > ID_dict[int(dests[1])]['d']:
                    del dests[0] 
        print(dests)
        
        break
    k+=1
    break

    

        
        
