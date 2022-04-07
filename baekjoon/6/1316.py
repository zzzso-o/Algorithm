N = int(input())
words = [input() for _ in range(N)]
bucket = [0] * len(words)
x = 1
for i in words:
    for j in range(len(words)):
        if i == words[j]:
            bucket[j] += x
        x += 1
print(bucket)
