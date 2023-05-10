import sys 
# sys.stdin = open('input1.txt')

def dfs(node):
    for n in arr[node]:
       if visited[n] == 0: # 방문 안했으면
            visited[n] = visited[node]+1 # 방문한걸로 바꿔주고
            dfs(n)

n = int(input())
a, b = map(int, input().split())
m = int(input())
visited = [0]*(n+1)
arr = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

dfs(a)
print(visited[b] if visited[b] > 0 else -1)