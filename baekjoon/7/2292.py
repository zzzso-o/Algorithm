N = int(input())
cnt = 1
bee_house = 1
while N > bee_house:
    bee_house += cnt*6
    cnt +=1
print(cnt)