import sys 
input = sys.stdin.readline

# prefix_sum
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0] # 인덱스가 헷갈리지 않게 0을 넣어준다.
# prefix_sum = [0, 5, 9, 12, 14, 15]

temp = 0
for i in numbers:
    temp += i
    prefix_sum.append(temp)
# 구간의 합을 미리 구해서 넣어준다.

for _ in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])
    # 구간 입력이 들어오면 구간합을 저장해 둔 리스트에서 위 연산을 수행하면 계산시간은 O(1)이 된다.
