from collections import deque
import sys
input = sys.stdin.readline
def push():
    total.appendleft(command[1])
def pop():
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
    if command[0] == 'push':
        push()
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()