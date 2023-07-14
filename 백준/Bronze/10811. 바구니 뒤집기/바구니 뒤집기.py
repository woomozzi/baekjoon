N ,M = map(int, input().split())
basket =[]
b = []
for k in range(1,N+1):
    basket.append(k)

for v in range(M) :
    i, j = map(int, input().split())
    b=basket[i-1 : j]
    b.reverse()
    basket[i-1 : j] = b
    
print(*basket)
