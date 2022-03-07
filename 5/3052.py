numbers = []
for _ in range(10):
    n = int(input())
    numbers.append(n % 42)

cnt = 0
for i in range(10):
    for j in range(i+1, 10):
        if numbers[i] == numbers[j]:
            cnt += 1
print(10 - cnt)