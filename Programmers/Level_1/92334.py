id0 = ["muzi", "frodo", "apeach", "neo"]
id1 = ["con", "ryan"]
re0 = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
re1 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k0 = 2
k1 = 3


def solution(id_list, report, k):
    report = [i.split(' ') for i in set(report)]
    id_dict = {string: 0 for string in id_list}
    answer = {string: 0 for string in id_list}
    for i in report:
        if i[1] in id_dict.keys():
            id_dict[i[1]] += 1
    for i in report:
        if id_dict[i[1]] >= k:
            answer[i[0]] += 1
    return list(answer.values())


print(solution(id0, re0, k0))
print(solution(id1, re1, k1))
