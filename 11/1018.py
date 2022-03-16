N, M = map(int, input().split())
arr = [input() for _ in range(N)]
# ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB',
# 'BWBBBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
ans = []
# 8*8로 잘라야 하므로 인덱스 크기 조절
# 9*9 보드에서 자를 수 있는 경우의 수 : 2
# 10*10 보드에서 자를 수 있는 경우의 수 : 3
# N * M 보드에서 자를 수 있는 경우의 수  : N-i * M-j
for i in range(N-7):
    for j in range(M-7):
        # 검은색으로 시작할 경우, 흰색으로 시작할 경우 초기화
        first_w = 0
        first_b = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                # 행과 열의 인덱스 합이 짝수인 애들끼리 같은 색을 가짐
                if (k+l) % 2 == 0:
                    if arr[k][l] != 'W':
                        first_w += 1
                    if arr[k][l] != 'B':
                        first_b += 1
                # 홀수일 경우
                else:
                    if arr[k][l] != 'B':
                        first_w += 1
                    if arr[k][l] != "W":
                        first_b += 1

        ans.append(first_w)
        ans.append(first_b)
print(min(ans))





# # 행 순회
# cnt = 0
# for i in range(M):
#     for j in range(N-1):
#         if arr[i][j] == arr[i][j+1]:
#             if arr[i][j] == 'B':
#                 arr[i][j+1] = 'W'
#                 cnt += 1
#             elif arr[i][j] == 'W':
#                 arr[i][j+1] = 'B'
#                 cnt += 1
# print(cnt)