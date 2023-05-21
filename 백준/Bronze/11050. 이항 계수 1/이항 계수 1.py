from itertools import combinations

n, k = map(int, input().split())
numbers = [_ for _ in range(n)]
c = list(combinations(numbers, k))
print(len(c))