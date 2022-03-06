N = int(input())
scores = list(map(int, input().split()))

for i in range(N):
    M = max(scores)
    scores[i] = scores[i] / M * 100
print(sum(scores)/N)