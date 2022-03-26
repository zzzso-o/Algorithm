N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
