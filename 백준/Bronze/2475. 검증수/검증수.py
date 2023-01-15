numbers = list(map(int, input().split()))
certi = 0
for i in range(5):
    certi += numbers[i]**2
print(certi%10)