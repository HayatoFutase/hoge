N = int(input())
s = [int(i) for i in input()]
#print(s)

def evaluation(a,b,c):
    nyan = [sum(a), sum(b), sum(c)]
    #print(max(nyan) - min(nyan))
    return max(nyan) - min(nyan)

score = float('inf')
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            a, b, c = s[:i]+s[k:], s[i:j], s[j:k]
            #print(a,b,c)
            score_ = evaluation(a, b, c)
            if score>score_:
                score=score_
            if score==0:
                break
        if score==0:
            break
    if score==0:
        break
print(score)
'''

def evaluation(min_, max_):
    return max_ - min_

score_ori = float('inf')
for i in range(N):
    pos = [i, i+int(N*(1/3)), i+int(N*(2/3))]
    a, b, c = sum(s[pos[2]:]+s[:pos[0]]), sum(s[pos[0]:pos[1]]), sum(s[pos[1]:pos[2]])
    #a, b, c = s[(i+int(N*(2/3))):]+s[:i], s[i:(i+int(N*(1/3)))], s[(i+int(N*(1/3))):(i+int(N*(2/3)))]
    min_ = min([a,b,c])
    max_ = max([a,b,c])
    if (min_==a) and (max_==b):
        score = evaluation(a,b)
        for j in range(1,N):
            a, b = sum(s[pos[2]:]+s[:pos[0]+j]), sum(s[pos[0]+j:pos[1]])
            score_ = evaluation(a,b)
            if (score>score_) and (score_>-1):
                score = score_
            else:
                break

    elif (min_==b) and (max_==a):
        score = evaluation(b,a)
        for j in range(1,N):
            a, b = sum(s[pos[2]:]+s[:pos[0]-j]), sum(s[pos[0]-j:pos[1]])
            score_ = evaluation(b,a)
            if (score>score_) and (score_>-1):
                score = score_
            else:
                break
    
    elif (min_==b) and (max_==c):
        score = evaluation(b,c)
        for j in range(1,N):
            b, c = sum(s[pos[0]:pos[1]+j]), sum(s[pos[1]+j:pos[2]])
            score_ = evaluation(b,c)
            if (score>score_) and (score_>-1):
                score = score_
            else:
                break
    
    elif (min_==c) and (max_==b):
        score = evaluation(c,b)
        for j in range(1,N):
            b, c = sum(s[pos[0]:pos[1]-j]), sum(s[pos[1]-j:pos[2]])
            score_ = evaluation(b,c)
            if (score>score_) and (score_>-1):
                score = score_
            else:
                break
    
    elif (min_==a) and (max_==c):
        score = evaluation(a,c)
    
    elif (min_==c) and (max_==a):
        score = evaluation(c,a)
    
    if score_ori>score:
        socre_ori = score

    if score_ori==0:
        break
print(score_ori)
'''
