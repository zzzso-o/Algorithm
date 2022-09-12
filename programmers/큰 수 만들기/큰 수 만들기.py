

def solution(number, k):
    cnt = 0
    answer = ''
    list_number = list(number)
    while cnt <= k:
        for i in range(len(number) - 1):
            if number[i] < number[i + 1]:

                cnt += 1

    return print(list_number)

solution("1924", 2)