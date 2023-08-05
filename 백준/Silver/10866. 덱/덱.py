from collections import deque
import sys
input = sys.stdin.readline
def push_front():
    total.append(command[1])
def push_back():
    total.appendleft(command[1])
def pop_back():
    if len(total) != 0:
        a = total.popleft()
        print(a)
    else :
        print(-1)
def pop_front():
    if len(total) != 0:
        a = total.pop()
        print(a)        
    else :
        print(-1)
def size():
    print(len(total))
def empty():
    if len(total) == 0:
        print(1)
    else:
        print(0)
def front():
    if len(total) != 0:
        print(total[-1])
    else:
        print(-1)
def back():
    if len(total) != 0:
        print(total[0])
    else:
        print(-1)

N = int(input())
total = deque()
for i in range(N):
    command =list(map(str,input().split()))
    if command[0] == 'push_front':
        push_front()
    elif command[0] == 'push_back':
        push_back()
    elif command[0] == 'pop_back':
        pop_back()
    elif command[0] == 'pop_front':
        pop_front()    
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()