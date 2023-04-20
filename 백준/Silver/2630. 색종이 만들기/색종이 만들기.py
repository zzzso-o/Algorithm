import sys
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
# print(paper)
result = []

def sol(x, y, N):
    color = paper[x][y]
    for i in range(x, N+x):
        for j in range(y, N+y):
            if color != paper[i][j]:
                sol(x, y, N//2)
                sol(x, y+N//2, N//2)
                sol(x+N//2, y, N//2)
                sol(x+N//2, y+N//2, N//2)
                return
    if color == 1:
        result.append(1)
    else:
        result.append(0)


sol(0, 0, N)
print(result.count(0))
print(result.count(1))