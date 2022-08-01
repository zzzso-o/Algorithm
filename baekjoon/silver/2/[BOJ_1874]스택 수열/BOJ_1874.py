import sys 
sys.stdin = open('input2.txt')
# input = sys.stdin.readline

stack = []
output = []
n = int(input())
cnt = 1
flag = False
numbers = [i for i in range(1, n+1)]
for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        output.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        output.append('-')
    else:
        print('NO')
        flag = True
        break

if flag == False:
    for i in output:
        print(i)