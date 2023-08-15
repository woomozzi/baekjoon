

from collections import deque
N = int(input())

for i in range(N):
    garo = input()
    total = deque()
    cnt = 0
    for j in garo:
        if j == '(':
            total.appendleft(j)
        if j == ')':
            if total:
                total.popleft()
            elif not total:
                cnt = 1
                break
    if not total and cnt == 0:
        print("YES")
    elif total or cnt > 0 :
        print("NO")