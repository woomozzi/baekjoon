import sys
N = int(input())
total = []
for i in range(N):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        total.append(command[1])
    elif command[0] == 2:
        if len(total) > 0:
            a = total.pop()
            print(a)
        else:
            print(-1)
    elif command[0] == 3:
        print(len(total))
    elif command[0] == 4 :
        if len(total) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 5 :
        if len(total) > 0:
            print(total[-1])
        else:
            print(-1)
