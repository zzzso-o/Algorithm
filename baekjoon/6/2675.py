import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    R, S = map(str, input().split())
    r = int(R)
    for i in S:
        print(i*r, end='')
    print()