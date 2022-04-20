n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

first = sorted(numbers)[-1]
second = sorted(numbers)[-2]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)