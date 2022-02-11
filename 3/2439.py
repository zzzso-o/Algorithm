N = int(input())

result = ''
for i in range(1, N+1):
    result = ((N-i)*' ') + (i * '*')
    print(result)

# 공백갯수, 빈문자열에 더하기 사용 