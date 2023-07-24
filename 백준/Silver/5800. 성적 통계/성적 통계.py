N = int(input())

for i in range(N):
    num = 1
    c1 = list(map(int, input().split()))
    del c1[0]
    c1.sort()
    cha2 = []
    for j in range(0, len(c1)-1):
        cha2.append(c1[j+1] - c1[j])
    ncha = max(cha2)
    
    print('Class',i+1)
    print('Max',str(max(c1))+',','Min',str(min(c1))+',',"Largest gap",ncha)