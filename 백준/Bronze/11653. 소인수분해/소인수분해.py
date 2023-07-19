N = int(input())
b = []
a = 2
while True :
    if N == 1:
        print(*b, sep='\n')
        break
    if N % a  == 0:
        N = N//a
        b.append(a)
    else :
        a += 1