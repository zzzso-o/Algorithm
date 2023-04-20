import sys 
# sys.stdin = open('input1.txt') 

n, m = map(int, input().split())
i = 1
y = 0 # 최소공배수
while True:
    if (n*i) % m == 0:
        y = n*i
        break
    else:
        i += 1
x = (n*m)//y # 최대공약수
print(x)
print(y)