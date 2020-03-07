# Input
N = int(input())    # Num of towns
bridges = [[int(i) for i in input().split(' ')] for j in range(N-1)]  # Bridges info.
#print(bridges)

cheese = [[float('inf') for i in range(N)] for j in range(N)]
for bridge in bridges:
    cheese[bridge[0]-1][bridge[1]-1] = bridge[2]
    cheese[bridge[1]-1][bridge[0]-1] = bridge[2]

lengthss = []
for i in range(N):
    lengths = [float('inf') for _ in range(N)]
    lengths[i] = 0
    able = [False for _ in range(N)]
    while True:
        point = -1
        for j in range(N):
            if (not able[j]) and (point==-1):
                point = j
            elif (not able[j]) and (lengths[j]<lengths[point]):
                point = j
        if point==-1:
            break
        able[point] = True

        for j in range(N):
            lengths[j] = min(lengths[j], lengths[point]+cheese[point][j])
    lengthss.extend(lengths)

#print(lengthss)
#print(sum(lengthss), sum(lengthss)/(len(lengthss)-N))
print(sum(lengthss)/(len(lengthss)-N))

