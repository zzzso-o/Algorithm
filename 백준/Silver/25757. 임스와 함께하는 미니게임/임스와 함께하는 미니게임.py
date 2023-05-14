import sys 
# sys.stdin = open('input3.txt')

N, a = map(str, input().split())
n = int(N)
people = set()
for _ in range(n):
    people.add(input().rstrip())

if a == "Y":
    print(len(people))
elif a == "F":
    print(len(people)//2)
else:
    print(len(people)//3)