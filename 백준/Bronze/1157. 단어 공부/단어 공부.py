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
# 먼저 변수 N를 설정하고 lower()를 이용해서 입력받은 문자열을 소문자로만 입력받고
# 이것을 set()을 이용해서 자료형의 중복을 제거한 뒤 list()로 리스트로 묶었다.
# 다음으로 가장 많이 사용된 알파벳을 알기 위해서 cnt 변수를 [] 리스트로 초기화하면 변수 설정 끝.
# N = mississipi
# setword = ['m', 'i', 's', 'p']
# 이제 setword안에 들어있는 각각의 문자들을 for문으로 반복해주는데
# count 변수를 새로 만들어서 중복되는 문자를 제외하기 전 입력받은 word 변수에서 그 문자가 몇 개 있었는지 count()를 이용해서 세고, cnt 변수 리스트에 append, 추가해준다.
# cnt = [4, 4, 1, 1]
# 그리고 if 문을 사용해서 만약 cnt 변수 리스트에 가장 큰 값 max(cnt)를 count() 함수를 이용해서 센 개수가
# cnt 변수 리스트 안에 2개 이상이라면! (말이 좀 복잡하지만 이해하고 넘어가셔야합니다....!!)
# 이 때는 가장 많이 사용된 알파벳, 즉 max(cnt)가 여러 개 존재하는 경우이기 때문에 "?"을 출력해준다.
# 그리고 그 나머지의 경우를 설명하기 위해서
# 예를 들어, 예제 입력 4의 경우
# N = baaa
# setword = [b, a]
# cnt = [1, 3]
# 위와 같은 코드에서 max(cnt)는 3이되고, index(3)은 cnt에서 cnt[1]에 위치하기 때문에
# 즉, index 자체가 가리키는 3이 cnt[1]이기 때문에 setword[1]은 a를 가리키는데
# 이것이 uppercase()로 인해 대문자로만 출력되기 때문에 A가 출력된다. 풀이 끄-읏!!
