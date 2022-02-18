A, B = map(int, input().split())
C = int(input())

if B + C >= 60:
    A = A + ((B + C) // 60)
    B = (B+C) % 60
    if A >= 24:
        A = 0
else:
    B = B+C
print(A, B)
