N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sort_A = sorted(A, reverse=True)
sort_B = sorted(B)
total = 0
for i in range(N):
    total += sort_B[i] * sort_A[i]

print(total)