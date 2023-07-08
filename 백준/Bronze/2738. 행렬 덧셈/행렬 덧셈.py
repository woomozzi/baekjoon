# 2738
N, M = map(int,input().split())

Mat1 =[[0 for _ in range(M)]for _ in range(N)]
Mat2 =[[0 for _ in range(M)]for _ in range(N)]
Mat3 =[[0 for _ in range(M)]for _ in range(N)]

for i in range(N) :
    cols = list(map(int, input().split()))
    for j in range(M) :
        Mat1[i][j] = cols[j]
for i in range(N) :
    cols = list(map(int, input().split()))
    for j in range(M) :
        Mat2[i][j] = cols[j]
for i in range(N) :
    for j in range(M) :
        Mat3[i][j] = Mat1[i][j] + Mat2[i][j]
for i in range(N) :
    for j in range(M) :
        print(Mat3[i][j], end=" ")
    print()


