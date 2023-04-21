def solution(name, yearning, photo):
    answer = []
    cnt = 0
    n = len(name)
    score = []
    for i in range(n):
        score.append([name[i], yearning[i]])
    
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            for k in range(n):
                if photo[i][j] == score[k][0]:
                    cnt += score[k][1]
        answer.append(cnt)
        cnt = 0
                    
    return answer