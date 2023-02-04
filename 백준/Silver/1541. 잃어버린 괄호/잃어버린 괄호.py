sik = input().split('-')
result = []
for i in sik:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    result.append(cnt)

for i in range(1, len(result)):
    result[0] -= result[i]
print(result[0])