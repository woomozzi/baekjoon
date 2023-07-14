C = int(input())

for i in range(C) :
    N = list(map(int, input().split()))
    a = []
    c = 0
    a = N[1:]
    b = 0

    b = (sum(a)/N[0])
    for j in a :
        if j > b :
            c += 1
    d = float(c/N[0])*100
    print(str("{:.3f}".format(d))+'%')
