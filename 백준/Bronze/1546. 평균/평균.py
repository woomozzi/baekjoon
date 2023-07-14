N = int(input())
A = list(map(int, input().split()))
b = max(A)
c = 0
for i in range(N) :
    c += (A[i] / b)*100
print(c/N)