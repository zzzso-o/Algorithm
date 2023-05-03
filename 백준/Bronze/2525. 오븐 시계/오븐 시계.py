import sys 
# sys.stdin = open('input3.txt')

a, b = map(int, input().split())
c = int(input())

t = b+c

if b+c >= 60:
    a += t//60
    if a >=24:
        a -= 24
    b = t%60
    print(a, b)
else:
    print(a, t)