# INPUT
N, M, Q = [int(i) for i in input().split(' ')]
membership_ = [[(int(k)-1) if i<2 else int(k) for i,k in enumerate(input().split(' '))] for j in range(M)]
query = [[str(k) if i==0 else (int(k)-1) for i,k in enumerate(input().split(' '))] for j in range(Q)]
#print(membership_)
#print(query)

membership = [[0 for i in range(N)] for j in range(N)]
for m in membership_:
    membership[m[0]][m[1]] = m[2]
    membership[m[1]][m[0]] = m[2]

#print(membership)

member = [False for i in range(N)]
for q in query:
    if q[0]=='+':
        member[q[1]] = True
    else:
        member[q[1]] = False
    count = 0
    #memberships = [[membership[i][j] if not (member[i]==member[j]) else 0 for i in range(N)] for j in range(N)]
    #memberships = max(max([[membership[i][j] if not (member[i]==member[j]) else 0 for i in range(N)] for j in range(N)]))
    memberships = max([max([membership[i][j] if not (member[i]==member[j]) else 0 for i in range(N)]) for j in range(N)])
    print(memberships)
