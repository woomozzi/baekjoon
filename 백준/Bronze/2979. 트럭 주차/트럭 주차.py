A,B,C = map(int, input().split())
ptime = []
ABC= []
res = 0
for  j in range(3):
    X , Y = map(int,input().split())
    for i in range(X, Y):
        ptime.append(i)
setime = set(ptime)
setime = list(setime)
for i in setime:
    if i in ptime:
        ABC.append(ptime.count(i))
for i in ABC :
    if i == 1:
        res+=i*A
    elif i == 2:
        res+=i*B
    else:
        res+=i*C
print(res)