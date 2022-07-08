import sys, heapq
sys.stdin = open('input1.txt') 
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, -x)
    else:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))

