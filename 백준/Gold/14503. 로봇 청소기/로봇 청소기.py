import sys
# sys.stdin = open('input2.txt')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
n, m = map(int, input().split()) # 방의 크기
r, c, d = map(int, input().split()) # r, c는 청소기 좌표, d는 방향(0북 1동 2남 3서)
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)
visited = [[0]*m for _ in range(n)]
cnt = 0
#출발지점 방문 체크
visited[r][c] = 1
cnt = 1

while True:
    flag = 0
    for _ in range(4): #4방향으로 돌린다
        d = (d+3)%4
        nx = r + dr[d]
        ny = c + dc[d]

        #범위 안에 들고 빈칸이면
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                flag = 1 # 청소했다는 뜻
                break
    if flag == 0:
        if arr[r-dr[d]][c-dc[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dr[d], c-dc[d]