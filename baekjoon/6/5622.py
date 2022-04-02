word = input()
dial = [0, 0, 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV','WXYZ']
result = 0
for i in word:
    for j in range(2, 10):
        if i in dial[j]:
            result += j+1
print(result)