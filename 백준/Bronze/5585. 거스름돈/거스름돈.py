taro = 1000
taromoney = int(input())
tarojibul = taro - taromoney
gmoney = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in gmoney:
    cnt += tarojibul // i
    tarojibul %= i
print(cnt)
 