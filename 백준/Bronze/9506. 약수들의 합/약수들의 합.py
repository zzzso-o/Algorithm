while True:
    n = int(input())
    a = []
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            a.append(i)
    if n == sum(a):
        print(n, " = ", " + ".join(str(i) for i in a), sep="")
    else:
        print(n, "is NOT perfect.")