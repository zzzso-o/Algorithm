import sys 
# sys.stdin = open('input1.txt') 

while True:
    tri = sorted(list(map(int, input().split())), reverse=True)
    if sum(tri) == 0:
        break
    if tri[0] < tri[1] + tri[2]:
        if len(set(tri)) == 1:
            print("Equilateral")
        elif len(set(tri)) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")