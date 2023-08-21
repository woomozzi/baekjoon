N, K = map(int, input().split())
E = N - K
if N == K or K == 0:
    print(1)
else:
    for i in range(N-1,0,-1):
        N *= i
    for i in range(E-1,0,-1):
        E *= i
    for i in range(K-1,0,-1):
        K *= i
    total = N//(K*(E))
    print(total)