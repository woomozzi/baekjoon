N = int(input())
cnt = 0
for _ in range(N):
    word = input().rstrip()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                cnt -= 1
                break
    cnt += 1
print(cnt)