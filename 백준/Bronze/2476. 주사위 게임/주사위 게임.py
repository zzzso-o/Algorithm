n = int(input())
result = []
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        result.append(10000 + a*1000)
    elif a == b:
        result.append(1000 + a*100)
    elif b == c:
        result.append(1000 + b*100)
    elif a == c:
        result.append(1000 + c*100)
    else:
        result.append(max(a, b, c)*100)
print(max(result))