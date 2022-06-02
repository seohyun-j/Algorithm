m = ['KAKAO', 'TOBEORNOTTOBEORTOBEORNOT', 'ABABABABABABABAB']


def solution(msg):
    answer = []
    dic = [chr(65 + i) for i in range(26)]
    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic.index(msg[w:c]) + 1)
            break
        if msg[w:c + 1] not in dic:
            dic.append(msg[w:c + 1])
            answer.append(dic.index(msg[w:c]) + 1)
            w = c

    return answer


for i in m:
    print(solution(i))
