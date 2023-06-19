n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key=lambda a: a[0]) # 시작 시간을 기준으로 정렬
arr = sorted(arr, key=lambda a: a[1]) # 끝나는 시간을 기준으로 정렬

last = 0 # 회의의 마지막 시간을 저장할 변수
count = 0 # 회의 개수를 저장할 변수

for i, j in arr:
    if i >= last: # 시작 시간이 회의의 마지막 시간보다 크거나 같을때
        count += 1
        last = j

print(count)