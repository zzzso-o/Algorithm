import sys
input = sys.stdin.readline

word = input()
bucket = []
for i in word:
    cnt = 0
    for j in range(len(word)):
        if i == word[j] or i == word[j].upper():
            cnt += 1
    bucket.append(cnt)

count = 0
for k in range(len(bucket)):
    if bucket[k] == max(bucket):
        count += 1
        if count >= 2:
            print('?')
            break
        else:
            print(word[k].upper())
            break