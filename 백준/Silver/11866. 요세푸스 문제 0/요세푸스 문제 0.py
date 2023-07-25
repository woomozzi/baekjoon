from collections import deque
N,K = map(int,input().split())
yosae = deque()
a = []
b = []
x = 0
cnt = 1

for i in range(1, N+1):
    yosae.append(i)

while len(b) != N:
    x = yosae.popleft()
    if cnt == K :
        b.append(x)
        cnt = 1
    else :
        yosae.append(x)
        cnt += 1
print('<',end='')
print(*b,sep=', ',end='')
print('>')
    