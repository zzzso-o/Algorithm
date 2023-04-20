import sys
input = sys.stdin.readline

M = int(input())
s = set()
full = set([i for i in range(1, 21)])
for _ in range(M):
    command = input().rstrip()
    if command[:5] == "empty":
        s = set()
        continue
    if command[:3] == "all":
        s = full
        continue
    else:
        com, num = command.split()
    if com == "add":
        s.add(int(num))
        continue
    if com == "remove":
        if len(s) > 0 and int(num) in s:
            s.remove(int(num))
        continue
    if com == "check":
        if int(num) in s:
            print(1)
        else:
            print(0)
        continue
    if com == "toggle":
        if int(num) in s:
            s.remove(int(num))
        else:
            s.add(int(num))