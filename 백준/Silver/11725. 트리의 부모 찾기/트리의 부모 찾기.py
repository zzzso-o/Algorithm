import sys 
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n+1)

queue = deque()
queue.append(1)
# print(graph)

def bfs():
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next] == 0:
                visited[next] = now
                queue.append(next)

bfs()
result = visited[2:]
for x in result:
    print(x)