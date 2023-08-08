import sys
input=sys.stdin.readline
from collections import deque

n, w, L = map(int, input().split())
tk = deque(map(int, input().split()))
bridge = deque([0]*w)
time  = 0

while tk :
    bridge.popleft()
    if sum(bridge) + tk[0] <= L:
        bridge.append(tk.popleft())
        time += 1
    else :
        bridge.append(0)
        time += 1
print(time + w)