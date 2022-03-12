S = int(input())
cnt = 1
n = 0
while True:
    n += cnt
    if n > S:
        print(cnt-1)
        break
    elif n == S:
        print(cnt)
        break
    cnt += 1