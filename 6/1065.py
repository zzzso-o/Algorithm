def hansu(x):
    cnt = 0
    if x < 100:
        for i in range(1, x+1):
            cnt += i
        return cnt
    elif x >= 100:
        cnt = 99
        for i in range(100, x+1):
            if (i//100)-((i%100)//10) == ((i%100)//10)-((i%100)%10):
                cnt += 1
        return cnt

N = int(input())
print(hansu(N))