numbers = list(map(int, input().split()))
if numbers[0] != numbers[1] and numbers[0] != numbers[2]:
    if numbers[1] != numbers[2]:
        print(max(numbers) * 100)
    else:
        print(1000 + numbers[1]*100)
elif numbers[0] == numbers[1] and numbers[0] != numbers[2]:
    if numbers[1] != numbers[2]:
        print(1000 + numbers[0]*100)
    else:
        print(1000 + numbers[0] * 100)
else:
    print(10000 + numbers[0]*1000)