N, M = map(int, input().split())
basket = []
for k in range(1, N+1):
    basket.append(k)
for trade in range(M) :
    i,j = map(int, input().split())
    basket[i-1],basket[j-1] = basket[j-1],basket[i-1]
print(*basket)
