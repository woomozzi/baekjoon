N = int(input())
info = []

for i in range(N):
    x , y= map(str,input().split()) 
    info.append([int(x),y])
info.sort(key = lambda x:int(x[0]))
for i in info:
    print(*i)
