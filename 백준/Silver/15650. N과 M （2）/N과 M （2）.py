import sys
from itertools import permutations

N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
permu = list(permutations(numbers, M))
result = [0 for _ in range(len(permu))]

for i in range(len(permu)):
    result[i] = list(permu[i])

for j in result:
    if j == sorted(j):
        print(*j)