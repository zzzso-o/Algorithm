import sys 
# sys.stdin = open('input1.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
check = []
for _ in range(n):
    s.add(input().strip())
cnt = 0
for _ in range(m):
    c = input().strip()
    if c in s:
        cnt += 1
print(cnt)