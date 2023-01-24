from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
d = deque()
for _ in range(N):
    order = input()
    if order[:1] == 's':
        print(len(d))
        continue
    elif order[:1] == 'e':
        if d:
            print(0)
        else:
            print(1)
        continue
    elif order[:1] == 'f':
        if d:
            print(d[0])
        else:
            print(-1)
        continue
    elif order[:1] == 'b':
        if d:
            print(d[-1])
        else:
            print(-1)
        continue
    elif order[:5] == "pop_f":
        if d:
            print(d.popleft())
        else:
            print(-1)
        continue
    elif order[:5] == "pop_b":
        if d:
            print(d.pop())
        else:
            print(-1)
        continue
    else:
        pp, num = order.split()
        if pp == "push_back":
            d.append(int(num))
            continue
        elif pp == "push_front":
            d.appendleft(int(num))
            continue

