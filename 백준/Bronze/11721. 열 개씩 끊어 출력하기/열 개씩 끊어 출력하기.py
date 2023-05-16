word = input()

for i in range(0, len(word), 10):
    if i+10 <= len(word):
        print(word[i:i+10])
    else:
        print(word[i::])