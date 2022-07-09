import sys, heapq
sys.stdin = open('input1.txt') 
# input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

    else:
        heapq.heappush(heap, (abs(x), x))