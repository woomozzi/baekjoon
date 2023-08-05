from collections import deque
import sys
input = sys.stdin.readline
def one():
    total.appendleft(command[1])
def two():
    total.append(command[1])
def three():
    if len(total) != 0:
        a = total.popleft()
        print(a)
    else :
        print(-1)
def four():
     if len(total) != 0:
        a = total.pop()
        print(a)
     else :
        print(-1)
def five():
    print(len(total))
def six():
    if len(total) == 0:
        print(1)
    else:
        print(0)
def seven():
    if len(total) != 0:
        print(total[0])
    else:
        print(-1)
def eight():
    if len(total) != 0:
        print(total[-1])
    else:
        print(-1)
N = int(input())
total = deque()
for i in range(N):
    command =list(map(int,input().split()))
    if command[0] == 1:
        one()
    elif command[0] == 2:
        two()
    elif command[0] == 3:
        three()
    elif command[0] == 4:
        four()
    elif command[0] == 5:
        five()
    elif command[0] == 6:
        six()
    elif command[0] == 7:
        seven()
    elif command[0] == 8:
        eight()