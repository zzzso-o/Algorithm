import sys 
input = sys.stdin.readline

T = int(input())
ps = ""
for _ in range(T):
    ps = input().rstrip()
    stack = []
    for i in ps:
        if stack:
            if stack[-1] == "(" and i == ")":
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
