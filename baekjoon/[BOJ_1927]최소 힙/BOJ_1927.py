import sys
import heapq
sys.stdin = open('input1.txt') 
input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, x)
    elif x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)



