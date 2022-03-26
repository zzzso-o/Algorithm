N = int(input())
scores = list(map(int, input().split()))
new_scores = []
for i in range(N):
    M = max(scores)
    new_scores.append(scores[i] / M * 100)
print(sum(new_scores)/N)