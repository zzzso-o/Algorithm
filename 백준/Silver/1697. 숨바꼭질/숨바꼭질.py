import sys 
# sys.stdin = open('input1.txt')
from collections import deque

def bfs(s, e):
    q = deque()
    q.append(s)
    while q:
        x = q.popleft()
        if x == e:
            print(visited[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= m and not visited[nx]:# visited[nx]는 언제나 false다. 그렇다면 if not visited[nx]는 언제나 True다 ???

                visited[nx] = visited[x] + 1
                q.append(nx)

n, k = map(int, input().split())
m = 10 ** 5 # 시간초과 나지 않게 수 제한
visited = [0] * (m + 1) # 이동하는 거리를 알기 위한 변수
# 나는 cnt 변수를 사용해서 더해서 구하려고 했지만 접근방법이 틀렸다.ㅜㅜ
# 원리는 이해가 되는데...이걸어케품?
# 그래프의 간선 수 == 동생을 찾기까지 걸리는 시간 ... ㅜ
# https://wook-2124.tistory.com/273 <- 참고 블로그
bfs(n, k)