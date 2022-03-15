# 생성자를 구하는 함수
def d(n):
    x = 0
    # str로 바꿔서 각 자리수 더하기
    a = list(str(n))
    for i in a:
        x = x + int(i)
    return n + x

# set에 넣어서 중복 제거하는 방법으로 셀프넘버 찾기
result = set()
for i in range(1, 10001):
    result.add(d(i))
numbers = set(range(1, 10000))
ans = numbers - result
for k in sorted(ans):
    print(k)


