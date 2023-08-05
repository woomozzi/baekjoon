N=list(map(int, input().split()))
res = 0
for i in N:
    res += i**2
print(res%10)