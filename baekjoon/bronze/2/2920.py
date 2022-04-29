# 31
music = list(map(int, input().split()))

result = 0
for i in range(8):
    if music[i] == i+1:
        result = 0
    elif music[i] == 8-i:
        result = 1
    else:
        result = 2

if result == 0:
    print('ascending')
elif result == 1:
    print('descending')
else:
    print('mixed')