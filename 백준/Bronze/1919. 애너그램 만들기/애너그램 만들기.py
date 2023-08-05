a = input()
b = input()
d1 = dict()
for i in a:
    if i not in d1.keys():
        d1[i] = 1
    else :
        d1[i] += 1
for i in b:
    if i not in d1.keys():
        d1[i] = -1
    else :
        d1[i] -= 1
res = 0 
for i in d1.values() :
    res += abs(i)
print(res)