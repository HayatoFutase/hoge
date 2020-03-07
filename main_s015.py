# INPUT
k, s, t = [int(i) for i in input().split(' ')]

def abc(string, k):
    if k==0:
        return string
    else:
        return 'A' + abc(string, k-1) + 'B' + abc(string, k-1)+'C'

string = 'ABC'
print(abc(string,k-1)[(s-1):t])
