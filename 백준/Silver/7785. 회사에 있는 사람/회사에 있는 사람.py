import sys 
# sys.stdin = open('input1.txt') 
input = sys.stdin.readline

n = int(input())
people = dict()
for _ in range(n):
    name, check = map(str, input().strip().split())
    if check == "enter":
        people[name] = check
    else:
        del people[name]

result = sorted(people, reverse=True)
for i in result:
    print(i)
