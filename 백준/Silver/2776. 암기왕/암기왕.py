T = int(input())
for _ in range(T):
    N = int(input())
    book1 = set(map(int, input().split()))
    M = int(input())
    book2 = list(map(int, input().split()))
    for i in book2:
        if i in book1:
            print('1')
        else:
            print('0')
