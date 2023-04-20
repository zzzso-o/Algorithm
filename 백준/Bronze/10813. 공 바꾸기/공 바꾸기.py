import sys 
# sys.stdin = open('input1.txt') 

n, m = map(int, input().split())
default = [_ for _ in range(1, n+1)]
temp = 0

for i in range(m):
    a, b = map(int, input().split())
    temp = default[a-1]
    default[a-1] = default[b-1]
    default[b-1] = temp

print(*default)