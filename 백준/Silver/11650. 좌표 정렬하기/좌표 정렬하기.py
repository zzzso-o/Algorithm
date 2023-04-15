import sys 
# sys.stdin = open('input1.txt') 

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])
s_arr = sorted(arr)
for i in range(n):
    print(*s_arr[i])