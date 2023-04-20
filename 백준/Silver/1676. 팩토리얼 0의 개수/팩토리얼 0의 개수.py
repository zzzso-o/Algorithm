N = int(input())
f = 1

for i in range(1, N+1):
    f *= i
num = str(f)
cnt = 0
for i in range(len(num)-1, 0, -1):
    if num[i] == "0":
        cnt += 1
    else:
        break

# if N == 0:
    # print(1)
# else:
print(cnt)