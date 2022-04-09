a, b, c = map(int, input().split())
i = 1
while i < (10**8) * 21:
    if c*i - (b*i + a) > 0:
        print(i)
        break
    elif c*i - (b*i +a) <= 0:

            print(-1)
            break