import sys 
# sys.stdin = open('input1.txt') 

n, m = map(int, input().split())
baguni = [0 for _ in range(n+1)]

for x in range(m):
    i, j, k = map(int, input().split())
    for y in range(i, j+1):
        baguni[y] = k

print(*baguni[1::])