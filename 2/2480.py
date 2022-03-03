numbers = list(map(int, input().split()))
if numbers[0] != numbers[1]:
    if numbers[1] != numbers[2]:
        print(max(numbers) * 100)
    elif numbers[1] == numbers[2]:
        print(10000 + numbers[1]*1000)
elif numbers[0] == numbers[1]:
    if numbers[1] != numbers[2]:
        print
