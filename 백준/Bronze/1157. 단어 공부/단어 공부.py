N = input().lower()
setword = list(set(N)) 
cnt = []
for i in setword :
    count = N.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2 :
    print("?")
else :
    print(setword[(cnt.index(max(cnt)))].upper())