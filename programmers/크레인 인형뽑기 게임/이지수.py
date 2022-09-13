def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                basket.append(board[i][move - 1])
                board[i][move - 1] = 0
                break
        if len(basket) > 1 and basket[-1] == basket[-2]:
            answer += 2
            basket = basket[:-2]
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))