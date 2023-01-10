import sys 
sys.stdin = open('input1.txt')


N = int(input())
words = []
for i in range(N):
    words.append(input())

clear = list(set(words))
result = sorted(clear)
result = sorted(result, key=len)
for i in result:
    print(i)