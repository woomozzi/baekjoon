N=int(input())
total = []
for i in range(N):
    a=int(input())
    total.append(a)
total.sort()
for i in total:
    print(i)