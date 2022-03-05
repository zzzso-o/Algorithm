n = 1
for _ in range(3):
    N = int(input())
    n *= N

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
bucket = [0] * 10
ans = str(n)
for i in numbers:
    for j in range(len(ans)):
        if ans[j] == i:
            bucket[int(i)] += 1
    print(bucket[int(i)])