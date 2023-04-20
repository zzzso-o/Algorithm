white = list(map(int, input().split()))
result = [0, 0, 0, 0, 0, 0]

result[0] = 1-white[0]
result[1] = 1-white[1]
result[2] = 2-white[2]
result[3] = 2-white[3]
result[4] = 2-white[4]
result[5] = 8-white[5]


print(*result)