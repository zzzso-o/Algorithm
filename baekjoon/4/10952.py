# A, B = map(int, input().split())

# while A and B == 0:
#     print(A + B)


        # 이거 왜안됨?


while 1:
    A, B = map(int, input().split())
    if (A == 0 and B == 0):
        break
    else:
        print(A + B)