from collections import deque
import sys
# sys.stdin = open('input1.txt')
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny]:
                arr[nx][ny] = 0
                q.append([nx, ny])

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    baechu_point = [tuple(map(int, input().split())) for _ in range(K)]
    # print(baechu_point)
    arr = [[0] * M for _ in range(N)]

    for i in range(K):
        a, b = baechu_point[i][0], baechu_point[i][1]
        arr[b][a] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                arr[i][j] = 0
                bfs(i, j)
                cnt += 1
    print(cnt)
