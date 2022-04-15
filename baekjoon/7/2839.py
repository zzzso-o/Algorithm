N = int(input())
cnt = 0
while N >= 0:
    if N % 5 == 0:
        cnt += (N //5)
        print(cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)

# 난 왜 이런 코드를 생각하지 못할까..
# 조금만 더 생각하면 생각이 날 법도 한데..