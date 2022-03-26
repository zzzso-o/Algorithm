T = int(input())
for _ in range(T):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]
    cnt = 0
    for i in range(1, len(scores)):
        if scores[i] > avg:
           cnt += 1
    rate = cnt/scores[0] *100
    print(f'{rate:.3f}%')