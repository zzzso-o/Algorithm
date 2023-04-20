import sys 
# sys.stdin = open('input1.txt')
from itertools import combinations

n = int(input())
colors = [_ for _ in range(n)]
c = list(combinations(colors, 2))
# print (c)
if n == 1:
    print(0)
else:
    print(len(c)*2)