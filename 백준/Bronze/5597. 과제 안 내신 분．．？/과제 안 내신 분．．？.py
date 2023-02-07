import sys

students = [i for i in range(1, 31)]
result = []
for _ in range(28):
    x = int(input())
    if x in students:
        students.remove(x)
result = sorted(students)
for i in range(2):
    print(result[i])