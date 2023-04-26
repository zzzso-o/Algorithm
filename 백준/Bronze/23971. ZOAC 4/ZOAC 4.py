import sys, math
# sys.stdin = open('input1.txt') 

h, w, n, m = map(int, input().split())
# h행w열 짜리 2차원 리스트를 만든다
# for문을 돌리며 가로는 n, 세로는 m 간격에 1을 넣는다.
# 1의 갯수를 count
# 2차원 리스트는 시간초과 발생

# 세로 : (h-1)/(n+1) + 1
# 가로 : (w-1)/(m+1) + 1

a = math.ceil(h/(n+1))
b = math.ceil(w/(m+1))
result = a*b
print(result)