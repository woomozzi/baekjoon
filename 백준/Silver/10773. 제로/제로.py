T = int(input())
total = []
for i in range(T):
    a = int(input())
    if a > 0 :
        total.append(a)
    else :
        total.pop()
print(sum(total))
