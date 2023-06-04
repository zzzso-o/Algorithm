import sys 
# sys.stdin = open('input2.txt')
from itertools import permutations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = []

p_list = list(permutations(cards, 3))

for i in range(len(p_list)):
    if sum(p_list[i]) <= m:
        result.append(sum(p_list[i]))
print(max(result))