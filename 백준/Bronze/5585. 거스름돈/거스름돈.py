import sys 
# sys.stdin = open('input2.txt')

coins = [500, 100, 50, 10, 5, 1]
cnt = 0
money = 1000 - int(input())

for i in coins:
    cnt += money // i
    money %= i


print(cnt)
