import sys 
# sys.stdin = open('input1.txt') 

plate = input().rstrip()
result = 10
for i in range(1, len(plate)):
    if plate[i] == plate[i-1]:
        result += 5
    elif plate[i] != plate[i-1]:
        result += 10

print(result)