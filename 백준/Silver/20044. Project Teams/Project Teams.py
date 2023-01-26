import sys 
input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))
sorted_students = sorted(students)
coding_power = []

for i in range(N):
    coding_power.append(sorted_students.pop(0) + sorted_students.pop(-1))

print(min(coding_power))