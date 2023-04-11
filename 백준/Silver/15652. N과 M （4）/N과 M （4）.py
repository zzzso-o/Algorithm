import sys 
# sys.stdin = open('input2.txt')
n, m = map(int, input().split())
result = []

def dfs(cnt, index):
    if cnt - 1 == m: #탈출조건
        print(' '.join(map(str, result)))
        return

    for i in range(index, n+1):
        result.append(i)
        dfs(cnt+1, i)
        result.pop()
dfs(1,1)