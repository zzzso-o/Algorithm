N = int(input())
people = list(map(int, input().split()))

# 정렬
n_people = sorted(people)
# 인출하는 데 필요한 시간
total = 0
for i in range(N):
    total += sum(n_people[:i+1])

print(total)