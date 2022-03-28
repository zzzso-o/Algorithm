# import sys
# sys.stdin = open('algo1_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    rabbits = [list(map(int, input().split())) for _ in range(m)]
    farm = [[0] * n for _ in range(n)] # 0으로 채워진 농장 만들기

    for z in range(m):
        x, y = rabbits[z][0], rabbits[z][1] # x, y 좌표 설정
        farm[x][y] += 1
        if rabbits[z][2] == 0: # 상으로 이동할때
            for i in range(1, n):
                dx1 = x - rabbits[z][3]*i
                if 0 <= dx1 < n:
                    farm[dx1][y] += 1
        elif rabbits[z][2] == 1: # 하로 이동할때
            for i in range(1, n):
                dx2 = x + rabbits[z][3]*i
                if 0 <= dx2 < n:
                    farm[dx2][y] += 1
        elif rabbits[z][2] == 2: # 좌로 이동할때
            for i in range(1, n):
                dy1 = y - rabbits[z][3]*i
                if 0 <= dy1 < n:
                    farm[x][dy1] += 1
        elif rabbits[z][2] == 3: # 우로 이동할때
            for i in range(1, n):
                dy2 = y + rabbits[z][3]*i
                if 0 <= dy2 < n:
                    farm[x][dy2] += 1

    #  토끼의 피해를 입은 구역(!= 0)을 cnt에 저장
    cnt = 0
    for i in range(n):
        for j in range(n):
            if farm[i][j] != 0:
                cnt += 1

    print(f'#{tc} {cnt}')