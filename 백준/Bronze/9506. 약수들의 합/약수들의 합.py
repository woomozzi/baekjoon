while True:
    a = []
    n = int(input())
    for i in range(1,n):
        if n%i == 0:
            a.append(i)
    if n == -1:
        break
    if sum(a) == n:
        ml = list(map(str,a))
        result = " + ".join(ml)
        print(sum(a),'=',result)
    else :
        print(n,'is NOT perfect.')
