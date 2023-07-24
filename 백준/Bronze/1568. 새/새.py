N = int(input())
k = 1
cnt = 0
while N > 0:
    N = N-k
    k += 1
    cnt += 1
    if k>N :
        k = 1
    
print(cnt)
    