import sys 
# sys.stdin = open('input4.txt')
from collections import deque
input = sys.stdin.readline
dx = [0, 1, 0, -1] # 위오아왼
dy = [1, 0, -1, 0]
def bfs(x, y):
    q = deque() # bfs돌리려면 우선 큐 만들어주기
    q.append((x, y)) # 시작지점 넣기
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 범위 안에 있을때
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))
            else:
                continue

    return arr[n-1][m-1]


n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(n):
    a = input().rstrip()
    for j in range(m):
        arr[i].append(int(a[j]))
# visited = [[0] * m for _ in range(n)]
print(bfs(0, 0))