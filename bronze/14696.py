import sys
sys.stdin = open('input1.txt')


N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    bucket_a = [0] * 5
    bucket_b = [0] * 5
    for i in range(1, len(A)):
        for j in range(5):
            if A[i] == j:
                bucket_a[j] += 1

    for i in range(1, len(B)):
        for j in range(5):
            if B[i] == j:
                bucket_b[j] += 1


    if bucket_a[4] != bucket_b[4]:
        if bucket_a[4] > bucket_b[4]: ans = 'A'
        else: ans = 'B'
    elif bucket_a[3] != bucket_b[3]:
        if bucket_a[3] > bucket_b[3]: ans = 'A'
        else: ans = 'B'
    elif bucket_a[2] != bucket_b[2]:
        if bucket_a[2] > bucket_b[2]: ans = 'A'
        else: ans = 'B'
    elif bucket_a[1] != bucket_b[1]:
        if bucket_a[1] > bucket_b[1]: ans = 'A'
        else: ans = 'B'
    else:
        ans = 'D'

    print(ans)