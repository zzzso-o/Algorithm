import sys
input = sys.stdin.readline

q = []
N = int(input())
for _ in range(N):
    order = input()
    if order[:1] == 's':
        print(len(q))
    elif order[:1] == 'e':
        if q:
            print(0)
        else:
            print(1)
    elif order[:1] == 'f':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order[:1] == 'b':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif order[:2] == 'po':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    else:
        push, num = order.split()
        q.append(int(num))