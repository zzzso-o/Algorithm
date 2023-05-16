Day = 0
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

x, y = map(int, input().split())
for i in range(x-1):
    Day += days[i]
Day = (Day + y -1) % 7

print(weeks[Day])