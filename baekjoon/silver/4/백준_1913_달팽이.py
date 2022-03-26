N = int(input())
target = int(input())

bucket = [[0] * N for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 상우하좌
num = N ** 2
i = 0
x, y = 0, 0

while True:
    bucket[x][y] = num
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= N or ny >= N or bucket[nx][ny] != 0 or nx <= -1 or ny <= -1:
        i += 1
        if i == 4:
            i = 0
        continue
    x, y = nx, ny
    num -= 1
    if num == 1:
        break
bucket[x][y] = 1
for i in range(N):
    for j in range(N):
        if bucket[i][j] == target:
            k, w = i+1, j+1
    print(*bucket[i])
print(k, w)
