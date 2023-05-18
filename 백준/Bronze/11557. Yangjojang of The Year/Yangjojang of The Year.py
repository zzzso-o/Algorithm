import sys
T = int(input())

for _ in range(T):
    n = int(input())
    name = []
    drinking = []
    for _ in range(n):
        a, b = map(str, input().split())
        name.append(a)
        drinking.append(int(b))
    l = drinking.index(max(drinking))
    print(name[l])