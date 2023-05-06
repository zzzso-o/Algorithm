import sys 
# sys.stdin = open('input4.txt')

k, n, m = map(int, input().split())

result = k*n-m
if result <0:
    print(0)
else:
    print(result)