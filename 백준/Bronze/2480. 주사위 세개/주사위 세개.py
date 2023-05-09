import sys 
# sys.stdin = open('input3.txt')

num = list(map(int, input().split()))

result = 0
if num[0] == num[1] == num[2]:
    result += 10000+(num[0]*1000)
elif num[0] == num[1]:
    result += (num[0]*100 + 1000)
elif num[0] == num[2]:
    result += (num[0] * 100 + 1000)
elif num[1] == num[2]:
    result += (num[1] * 100 + 1000)
else:
    result += max(num)*100

print(result)