scores = []
for _ in range(8):
    scores.append(int(input()))

s_scores = sorted(scores, reverse=True)
print(sum(s_scores[:5]))
result = []
for i in range(5):
    result.append(scores.index(s_scores[i])+1)
print(*sorted(result))