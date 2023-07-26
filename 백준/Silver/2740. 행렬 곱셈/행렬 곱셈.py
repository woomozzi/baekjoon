N, M = map(int, input().split())
A = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    cols = list(map(int, input().split()))
    for j in range(M):
        A[i][j] = cols[j]

O, P = map(int, input().split())
B = [[0 for _ in range(P)] for _ in range(O)]
for i in range(O):
    cols2 = list(map(int, input().split()))
    for j in range(P):
        B[i][j] = cols2[j]

C = [[0 for _ in range(P)] for _ in range(N)]

for i in range(N):
    for j in range(P):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(*row)