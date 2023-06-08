import sys
# sys.stdin = open('input1.txt')
from collections import deque

m, n, k = map(int, input().split())
arr = [[0]*n for _ in range(m)]
result = []
# 직사각형 색칠
for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            arr[j][i] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    arr[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = 1 # 방문체크
                cnt += 1 # 너비
                q.append((nx, ny))
    result.append(cnt)

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            bfs(i, j)
print(len(result))
print(*sorted(result))