from sys import stdin
from collections import Counter 

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

result = []

C = Counter(cards)
print(' '.join(f'{C[ans]}' if ans in C else '0' for ans in find))