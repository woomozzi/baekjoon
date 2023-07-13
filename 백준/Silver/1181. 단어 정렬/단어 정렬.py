N = int(input())
word = []
for _ in range(N):
    a = input()
    word.append(a)
word = set(word)
word = list(word)
word.sort()
word.sort(key=len)
print(*word, sep='\n')