total = set()
num = set(range(1, 10001))
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    total.add(i)
selfnum = sorted(num - total)
for i in selfnum:
    print(i)
