n = int(input())
number = int(input()) 
direction =[[1,0],[0,1],[-1,0],[0,-1]] 
snail = [[0 for _ in range(n)] for _ in range(n)]
start = n * n 
curr_y = 0
curr_x = 0
curr_dir = 0 
solution = list()
for _ in range(n * n):
    if start == number:
        solution = [curr_y + 1, curr_x + 1]
    snail[curr_y][curr_x] = start 
    next_y = curr_y + direction[curr_dir][0] 
    next_x = curr_x + direction[curr_dir][1]
    if next_y < 0 or next_x < 0 or next_y >= n or next_x >= n or \
        snail[next_y][next_x] != 0:
        curr_dir += 1
        curr_dir = curr_dir % 4 
    curr_y = curr_y + direction[curr_dir][0]
    curr_x = curr_x + direction[curr_dir][1]
    start -= 1
for y in range(n):
    for x in range(n):
        print(snail[y][x], end=' ')
    print()
print(solution[0], solution[1])