numbers = []
for _ in range(9):
    n = int(input())
    numbers.append(n)
for i in range(9):
    if numbers[i] == max(numbers):
        print(max(numbers))
        print(i+1)
