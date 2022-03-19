# 생성자를 구하는 함수
def d(n):
    x = 0
    a = list(str(n))
    for i in a:
        x = x + int(i)
    return n + x

result = 0
for i in range(1, 10001):
    result.add(d(i))
numbers = set(range(1, 10000))
ans = numbers - result
for k in sorted(ans):
    print(k)