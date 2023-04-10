import sys 


input = sys.stdin.readline

n = int(input())
d = [0]*(n+1) # 인덱스가 1이 되는데 필요한 연산의 최솟값
for i in range(2, n+1): # 2~x까지 반복
    d[i] = d[i-1] + 1 # 을 빼는 연산 -> 1회추가
    if i % 2 == 0: # 2로 나누어 떨어질 때, 2로 나누는 연산
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0: # 3으로 나누어 떨어질 때, 3으로 나누는 연산
        d[i] = min(d[i], d[i//3]+1)
print(d[n])

#if i%2==0:    d[i]=min(d[i],d[i//2]+1)
# i가 2로 나누어 떨어질 때, d[i]와 d[i//2]+1중 최솟값을 d[i]에 저장한다.
# d[i//2]는 i가 2로 나누어떨어진다. -> i를 2로 나눈 값이 1이 되는데 걸리는 최소한의 연산 횟수