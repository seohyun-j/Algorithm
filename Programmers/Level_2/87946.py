k0 = 80
d0 = [[80, 20], [50, 40], [30, 10]]

from itertools import permutations


def solution(k, dungeons):
    queue = list(permutations(dungeons, len(dungeons)))
    answer = 0
    for i in queue:
        cnt = 0
        tmp = k
        for j in i:
            x, y = j
            if x <= tmp:
                tmp -= y
                cnt += 1
        answer = max(answer, cnt)
        if answer == len(dungeons):
            return answer
    return answer


print(solution(k0, d0))
