from random import choice
a=[ [8,1,6],
    [3,5,7],
    [4,9,2]]
def check(a):
    h=0
    v=0
    d=0
    g=0
    if sum(a[0])==sum(a[1])==sum(a[2]):
        h=1
    if sum([a[0][0],a[1][0],a[2][0]])==sum([a[0][1],a[1][1],a[2][1]])==sum([a[0][2],a[1][2],a[2][2]]):
        v=1
    if sum([a[0][0],a[1][1],a[2][2]])==15:
        d=1
    if sum([a[0][2],a[1][1],a[2][0]])==15:
        g=1
    if g and d and h and v:
        return True
    return False

dic={}
while 1:
    lis=[i for i in range(1,10)]
    l=[]
    for i in range(3):
        le=[]
        for j in range(3):
            ll=random.choice(lis)
            le.append(ll)
        l.append(le)
    print(l)
    break


