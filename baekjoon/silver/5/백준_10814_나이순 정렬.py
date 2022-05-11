N = int(input())

members = [list(map(str, input().split())) for _ in range(N)]
s_members = sorted(members)
# print(s_members)
# print(members)
result = []
