N = int(input())

i = 1
while i <= N:
    if N % 5 == 0:
        print(N//5)
    elif N % 5 != 0:
        N -= 5*i

