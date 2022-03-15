def d(n):
    return n + (n//10) + (n%10)


numbers = set(range(1, 10001))
rmv = set()
for i in range(1, 10001):
    rmv.add(d(i))
numbers = numbers - rmv
for j in sorted(numbers):
    print(j)