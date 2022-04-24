arr = [list(map(int, input().split())) for _ in range(3)]
ans = []

for i in range(3):
    if arr[0][0] - arr[i][0] != 0 or arr[1][0] - arr[i][0] != 0 or arr[2][0] - arr[i][0] != 0:
        ans.append(arr[i][0])
    elif arr[0][1] - arr[i][1] != 0 or arr[1][1] - arr[i][1] != 0 or arr[2][1] - arr[i][1] != 0:
        ans.append(arr[i][1])
print(ans)