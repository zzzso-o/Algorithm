N = int(input())
group_word = 0
for _ in range(N):
    word = input()
    error = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]: # 바로 옆 글자랑 다르다면
            new_word = word[i+1::] # 인덱스 뒤에 글자를 새 문자열로 저장
            if word[i] in new_word: # 인덱스 문자가 새 문자열에 있다면
                error += 1 # 그룹단어 아님
    if error == 0: # 이면 그룹단어
        group_word += 1
print(group_word)