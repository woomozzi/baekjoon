N = int(input())
info =[]
rank = []
for i in range(N) :
    x,y = map(int, input().split())
    info.append([x,y])

for i in range(N) :
    c = 1
    for k in range(N) :
        if info[i][0] < info[k][0] and info[i][1] < info[k][1] :
            c += 1
    rank.append(c)
print(*rank)
#때려쳐
    