import sys 
input=sys.stdin.readline
N = int(input())
sang_card = list(map(int, input().split()))
M = int(input())
num_card = list(map(int, input().split()))

dicard = {}
for i in range(N):
    dicard[sang_card[i]] = 0
for j in range(M):
    if num_card[j] not in dicard:
        print(0, end='\n')
    else :
        print(1, end='\n')