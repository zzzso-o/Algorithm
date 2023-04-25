import sys 
# sys.stdin = open('input1.txt') 

text = []
for _ in range(5):
    text.append(input())

for i in range(max(len(e) for e in text)):
    for j in range(5):
        if i < len(text[j]): # 글자수체크 (i) 보다 text[j]길이가 짧으면 text[j]의 i번째가 없다는 뜻
            # 건너뛰고 i보다 클때만 출력한다.
            print(text[j][i], end='')