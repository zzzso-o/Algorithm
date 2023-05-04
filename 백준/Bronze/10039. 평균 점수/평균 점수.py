import sys 
# sys.stdin = open('input1.txt') 

score = []
for _ in range(5):
    x = int(input())
    if x < 40:
        x = 40
    score.append(x)

print(sum(score)//5)