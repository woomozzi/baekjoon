M = int(input())
N = int(input())

soSu = []

def sosu(da) :
    da_2 = int(da**0.5)
    for k in range(2, da_2+1) :
        if da % k == 0:
            return False
    return True

for i in range(M, N+1):
    if i == 1:
        continue
    if sosu(i) :
        soSu.append(i)

if not soSu :
    print(-1)
else :
    print(sum(soSu))
    print(min(soSu))