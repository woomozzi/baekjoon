import sys
input=sys.stdin.readline
N=int(input())
total=[]
for i in range(N):
    a =int(input())
    total.append(a)
total.sort()

for j in total:
    print(j)
    