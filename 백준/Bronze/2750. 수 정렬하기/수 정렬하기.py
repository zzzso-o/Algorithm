n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()

for i in range(n):
    print(numbers[i])