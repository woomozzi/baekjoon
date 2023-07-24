n = int(input())
nachi = []
while True :
    for i in range(n+1):
        if len(nachi) >= 2:
            nachi.append(nachi[i-1] + nachi[i-2])
        else:
            nachi.append(i)
    print(nachi[n])
    break
   