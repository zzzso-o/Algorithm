A, B = map(str, input().split())
a, b = A[::-1], B[::-1]

if a < b:
    print(b)
else:
    print(a)