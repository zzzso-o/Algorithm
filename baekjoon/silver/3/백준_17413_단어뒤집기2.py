s = input()
result = []
tags = []

for i in range(len(s)):
    if s[i] == '<':
        for j in range(len(s)):
            if s[j] == '>':
                tags.append(s[i:j+1])
            elif s[j] == '<':
                result.append
