N = int(input())
group_word = 0
for _ in range(N):
    word = input()
    error = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1::]
            if word[i] in new_word:
                error += 1
    if error == 0:
        group_word += 1

print(group_word)