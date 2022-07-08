import sys
from collections import deque
sys.stdin = open('input1.txt') 

def bfs(start):
    while start == K:
        return
    if start * 2 < K - start:
        start *= 2
    else:




N, K = int(input().split())
time = 0
