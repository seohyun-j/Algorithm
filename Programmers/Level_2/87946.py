k0 = 80
d0 = [[80, 20], [50, 40], [30, 10]]

from itertools import permutations


def solution(k, dungeons):
    answer = []
    seq = list(permutations([i for i in range(len(dungeons))], len(dungeons)))

    for i in seq:
        sum = 0
        keys = k

    return answer


print(solution(k0, d0))