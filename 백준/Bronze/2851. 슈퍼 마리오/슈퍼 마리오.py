MR = []
MR100 = []
MRsum = []
c = 0
result = []
for _ in range(10):
    a = int(input())
    MR.append(a)
for k in range(len(MR)):
    MRsum.append(sum(MR[:k+1]))
for i in range(len(MR)):
    MR100.append(abs(MRsum[i] - 100))
for j in range(len(MR)):
    if MR100[j] == min(MR100):
        result.append(j)
c = max(result)
print(MRsum[c])