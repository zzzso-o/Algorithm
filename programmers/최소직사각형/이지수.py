def solution(sizes):
    answer = 0
    max_w = []
    max_h = []
    new_sizes = []
    for i in range(len(sizes)):
        new_sizes.append(sorted(sizes[i]))
    
    for i in range(len(sizes)):
        max_w.append(new_sizes[i][0])
        max_h.append(new_sizes[i][1])
    answer = max(max_h) * max(max_w)
        
    return answer