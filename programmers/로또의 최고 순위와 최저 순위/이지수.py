def solution(lottos, win_nums):
    cnt = 0
    zero= 0
    for i in lottos:
            if i == 0:
                zero += 1
            if i in win_nums:
                cnt += 1
            
                
    answer = [0,0]    
    for i in range(1, 7):
        if cnt + zero < 2:
            answer[0] = 6
        if cnt + zero == i:
            answer[0] = (6-i+1)
        if cnt < 2:
            answer[1] = 6
        if cnt == i:
            answer[1] = 6-i+1
    

    return answer