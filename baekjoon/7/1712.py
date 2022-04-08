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
