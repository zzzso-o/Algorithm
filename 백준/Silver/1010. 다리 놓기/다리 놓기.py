import sys
# import time

# sys.stdin = open('input1.txt') 
# start = time.time()
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    # mCn
    # mCn = m! / n! * (m-n)!
    mi = 1
    ni = 1
    m_n = 1
    for i in range(1, m+1):
        mi *= i
    for j in range(1, n+1):
        ni *= j
    for k in range(m-n, 1, -1):
        m_n *= k
    print(mi//(ni*m_n))
# print("time: ", time.time()-start)