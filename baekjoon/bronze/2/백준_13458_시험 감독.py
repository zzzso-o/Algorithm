# 12
import math

N = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0

for i in range(N):
    new = a[i] - b
    cnt += 1
    if new > 0:
        cnt += math.ceil(new / c)
print(cnt)