n = int(input())
m = int(input())

emplist = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    emplist[x].append(y)
    emplist[y].append(x)

virus = [0 for _ in range(n+1)]
# virus = [0]*(n+1)

def virusdfs(demplist, v, dvirus):
    virus[v] = 1
    for i in demplist[v] :
        if virus[i] == 0:
            virusdfs(demplist, i, dvirus)
virusdfs(emplist, 1, virus)
print(virus.count(1)-1)