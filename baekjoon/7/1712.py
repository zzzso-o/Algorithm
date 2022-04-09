<<<<<<< HEAD
a, b, c = map(int, input().split())
i = 1
while i < (10**8) * 21:
    if c*i - (b*i + a) > 0:
        print(i)
        break
    elif c*i - (b*i +a) <= 0:

            print(-1)
            break
=======
import sys
a, b, c = map(int, sys.stdin.readline().split())

'''
x = 1
while True:
    if b > c:
        print(-1)
        break
    elif c * x - (b * x + a) > 0:
        print(x)
        break
    else:
        x += 1
'''

if b >= c:
    print(-1)
else:
    print(int(a/(c-b)+1))
>>>>>>> 645c490311165d4abbd62b24b2c9036aaa74a7ee
