namozi = []
for i in range(10) :
    a = int(input())
    b = a % 42
    namozi.append(b)
namozi = set(namozi)
print(len(namozi))
