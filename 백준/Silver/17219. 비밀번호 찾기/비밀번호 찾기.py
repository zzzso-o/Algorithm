import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memos = {}
sites = {}
for _ in range(N):
    site, pw = input().split()
    memos[site] = pw

for _ in range(M):
    print(memos[input().rstrip()])