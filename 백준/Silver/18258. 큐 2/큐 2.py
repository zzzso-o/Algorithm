from collections import deque
import sys
input = sys.stdin.readline
que = deque()
N = int(input())
for _ in range(N):
    order = input()
    if order[:2] == "pu":
        push, num = order.split()
        que.append(int(num))
        continue
    elif order[:2] == "po":
        if que:
            print(que.popleft())
        else:
            print(-1)
        continue
    elif order[0] == "s":
        print(len(que))
        continue
    elif order[0] == "e":
        if que:
            print(0)
        else:
            print(1)
        continue
    elif order[0] == "f":
        if que:
            print(que[0])
        else:
            print(-1)
        continue
    elif order[0] == "b":
        if que:
            print(que[-1])
        else:
            print(-1)
        continue
