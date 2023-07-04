n = int(input())
c = 0
nc = 0
for _ in range(n):
    x = int(input())
    if x == 1:
        c += 1
    else:
        nc += 1
if c > nc:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")