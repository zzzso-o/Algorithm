arr = [list(map(int, input().split())) for _ in range(3)]
ans = []

for i in range(2):
    if arr[0][i] != arr[1][i] and arr[0][i] != arr[2][i]:
        ans.append(arr[0][i])
    elif arr[1][i] != arr[0][i] and arr[1][i] != arr[2][i]:
        ans.append(arr[1][i])
    elif arr[2][i] != arr[0][i] and arr[2][i] != arr[1][i]:
        ans.append(arr[2][i])

print(*ans)