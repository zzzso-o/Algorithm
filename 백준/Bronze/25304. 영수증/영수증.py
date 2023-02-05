import sys 

x = int(input())
n = int(input())
result = []
for _ in range(n):
    a, b = map(int, input().split())
    result.append(a*b)

if sum(result) == x:
    print("Yes")
else:
    print("No")