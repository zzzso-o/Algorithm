import sys 
sys.stdin = open('input1.txt')
# 색종이의 수
N = int(input())
# papers = []
# intersection = 0
# total = N * 100
# for _ in range(N):
#     papers.append(list(map(int, input().split())))
#
# for i in range(N):
#     for j in range(i, N-1):
#         if abs(papers[i][0] - papers[j+1][0]) < 10:
#             if abs(papers[i][1] - papers[j+1][1]) < 10:
#                 x = 10 - abs(papers[i][0] - papers[j+1][0])
#                 y = 10 - abs(papers[i][1] - papers[j+1][1])
#                 intersection += x*y

papers = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            papers[i][j] = 1

answer = 0
for row in papers:
    answer += row.count(1)
print(answer)
