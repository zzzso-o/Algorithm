T = int(input())
for tc in range(T):
    result = list(input())
    cnt = 0
    total = []
    for i in range(len(result)):
        if result[i] == 'O':
            cnt += 1
            total.append(cnt)
        elif result[i] == 'X':
            cnt = 0
    print(sum(total))