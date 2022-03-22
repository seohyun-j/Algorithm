r = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]


def solution(record):
    record = [i.split(' ') for i in record]
    nickname = {}
    answer = []
    for i in record:
        if i[0] == "Enter" or i[0] == "Change":
            nickname[i[1]] = i[2]
    for i in record:
        if i[0] == "Enter":
            answer.append(nickname[i[1]] + '님이 들어왔습니다.')
        elif i[0] == "Leave":
            answer.append(nickname[i[1]] + '님이 나갔습니다.')
    return answer


print(solution(r))
