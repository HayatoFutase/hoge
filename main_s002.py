# INPUT
M, N = [int(i) for i in input().split(' ')] # M:column
cheese = []
for j in range(N):
    c = []
    for i,s in enumerate(input().split(' ')):
        c.append(s)
        if s=='s':
            start = [j, i]
        elif s=='g':
            goal = [j, i]
        cheese.append(c)
#print(M,N)
#print(cheese)
'''
f = open('sample1.txt')
M, N = [int(i) for i in f.readline().rstrip('\n').split(' ')] # M:column
cheese = []
for j in range(N):
    c = []
    for i,s in enumerate(f.readline().rstrip('\n').split(' ')):
        c.append(s)
        if s=='s':
            start = [j, i]
        elif s=='g':
            goal = [j, i]
    cheese.append(c)

#print(cheese)
'''
distance = [[float('inf') for i in range(M)] for j in range(N)]
point = []
point.insert(0, start)
distance[start[0]][start[1]] = 0

count = 0
while True:
    count+=1
    #print(count)
    #print(distance)
    if len(point)==0:
        break
    n, m = point.pop()
    if n==goal[0] and m==goal[1]:
        break
    for i in range(0,4):
        n_, m_ = n + [1,0,-1,0][i], m + [0,1,0,-1][i]
        #print(m,m_)
        if m_>=0 and m_<M and n_>=0 and n_<N and (not cheese[n_][m_]=='1') and distance[n_][m_]==float('inf'):
            point.insert(0, [n_,m_])
            distance[n_][m_] = distance[n][m] + 1

if distance[goal[0]][goal[1]]==float('inf'):
    print('Fail')
else:
    print(distance[goal[0]][goal[1]])
