h, m = input().split()
H = int(h)
M = int(m)

# 45보다 작은 경우
if M < 45 and H == 0:
    print(23, (M+60)-45)
elif M < 45 and H > 0:
    print(H-1, (M+60)-45)
elif M >= 45:
    print(H, M-45)