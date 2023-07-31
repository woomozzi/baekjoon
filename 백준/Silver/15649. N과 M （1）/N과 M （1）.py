N,M = map(int, input().split())
N_list = [i for i in range(1, N+1)]
temp = []

def backtrack():
    if len(temp) == M:
        print(*temp)
        return
    for i in range(N):
        if N_list[i] not in temp:
            temp.append(N_list[i])
            backtrack()
            temp.pop()
backtrack()