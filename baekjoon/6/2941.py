croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
text = input()
for i in croatia:
    text = text.replace(i, 'a')
print(len(text))

# replace 함수를 쓰면 쉽게 해결할 수 있었던 문제
# text 안 크로아티아 문자를 찾아서 a로 대체한 후 text의 길이를 출력한다...
# 개빡침