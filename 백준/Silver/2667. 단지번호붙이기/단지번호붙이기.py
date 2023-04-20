import sys
from collections import deque
# sys.stdin = open('input1.txt') 

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(house, a, b):
    n = len(house)
    queue = deque()
    queue.append((a, b))
    house[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if house[nx][ny] == 1:
                house[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

n = int(input())
house = []
for i in range(n):
    house.append(list(map(int, input().rstrip())))

cnt = []
for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            cnt.append(bfs(house, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])