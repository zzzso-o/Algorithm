import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    A, B = map(int,input().split())
    print(A + B)


# sys.stdin.readline 모듈 사용. split도 할 수 있음
# 길기 때문에 변수 할당해두는 것이 좋음