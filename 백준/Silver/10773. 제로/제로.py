import sys 

K = int(input())
result = []
for _ in range(K):
    x = int(input())
    if x == 0:
        result.pop()
    else:
        result.append(x)


print(sum(result))