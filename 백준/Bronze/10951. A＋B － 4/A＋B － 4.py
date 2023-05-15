import sys
# sys.stdin = open("input1.txt")

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break