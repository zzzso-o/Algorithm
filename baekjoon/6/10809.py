S = input()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in alphabet:
    for j in range(len(S)):
        if i not in S:
            print(-1,end=' ')
            break
        else:
            if i == S[j]:
                print(j,end=' ')
                break