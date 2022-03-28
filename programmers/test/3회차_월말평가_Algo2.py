import sys
sys.stdin = open('algo2_sample_in.txt')

# 재귀함수..
def get_ddang(x, y):
    global N, ddang
    if ddang[x][y] != 0:
        pass

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ddang = [list(map(int, input().split())) for _ in range(N)]

    ddang_price = 0
    cnt = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            if ddang[i][j] != 0:
                ddang_price += ddang[i][j]
                cnt += 1
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    if ddang[ni][nj] != 0:
                        ddang_price += ddang[ni][nj]
                        cnt += 1