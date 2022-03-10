S = int(input())

cnt = 0 # 더한 횟수
n = 0 # 자연수 더한값
for i in range(1, S+1):
    cnt += 1
    n += i
    if n > S: # 합이 S보다 커지면
        cnt -= 1
        # 더하는 횟수에서 하나만 빼주면 된다.
        break
print(cnt)

'''
S = int(input())
cnt = 1
n = 0
while True:
    n += cnt
    if n > S:
        print(cnt-1)
        break
    elif n == S:
        print(cnt)
        break
    cnt += 1
'''