def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)] # 미로의 크기만큼 생성
    queue = [] # 큐 생성
    queue.append((i, j)) # 시작점 인큐
    visited[i][j] = 1 # 시작점 방문 표시
    while queue: # 큐가 비어있지 않으면 반복
        i, j = queue.pop(0) # t <- 디큐
        if maze[i][j] == 3: # visited(t) t에서 할 일 처리
            return visited[i][j] -2 # 출발 도착 칸 제외
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # i, j에 인접한 칸에 대해
            ni, nj = i+di, j+dj # 주변 칸 좌표, 미로를 벗어나지 않고, 인접(벽이 아님)
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0: # 순서바뀌면 안됨. 순서대로 처리함
                queue.append((ni, nj)) # 인큐
                visited[ni][nj] = visited[i][j] + 1
    return 0 # 도착지를 찾지 못한 경우

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = fstart(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')