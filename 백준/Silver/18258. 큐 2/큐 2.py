from collections import deque
import sys
N = int(input())
total = deque([])
for i in range(N):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == 'push':
        total.append(command[1])
    elif command[0] == 'pop':
        if len(total) == 0:
            print(-1)
        else:
            print(total.popleft())
    elif command[0] == 'size':
        print(len(total))
    elif command[0] == 'empty' :
        if len(total) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front' :
        if len(total) == 0:
            print(-1)
        else :
            print(total[0])
    elif command[0] == 'back' :
        if len(total) == 0:
            print(-1)
        else:
            print(total[-1])
