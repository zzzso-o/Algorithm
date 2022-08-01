# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

def solution(id_list, report, k):
    n = len(id_list)
    answer = [0] * n
    user_report = [[] for _ in range(n)]
    new_report = []
    temp = [0] * n

    for i in report:
        new_report.append(i.split(' '))

    for i in range(n):
        for j in range(len(new_report)):
            if id_list[i] == new_report[j][0]:
                if not new_report[j][1] in user_report[i]:
                    user_report[i].append(new_report[j][1])

    for i in range(n):
        for j in range(n):
            if id_list[i] in user_report[j]:
                temp[i] += 1

    for i in range(n):
        if temp[i] >= k:
            for j in range(n):
                if id_list[i] in user_report[j]:
                    answer[j] += 1

    return  print(answer)

solution(id_list, report, k)