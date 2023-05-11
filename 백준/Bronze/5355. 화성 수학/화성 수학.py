import sys 
# sys.stdin = open('input1.txt') 

T = int(input())
for _ in range(T):
    result = list(map(str, input().split()))
    a = float(result[0])
    for i in range(1, len(result)):
        if result[i] == "@":
            a *= 3
        elif result[i] == "%":
            a += 5
        elif result[i] == "#":
            a -= 7
    print(format(a, ".2f"))