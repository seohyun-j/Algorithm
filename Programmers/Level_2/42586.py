p0 = [93, 30, 55]
p1 = [95, 90, 99, 99, 80, 99]
s0 = [1, 30, 5]
s1 = [1, 1, 1, 1, 1, 1]

import math


def solution(progresses, speeds):
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    result = []
    lenth = 1
    max_idx = progresses[0]

    for i in range(1, len(progresses)):
        if max_idx >= progresses[i]:
            lenth += 1
        elif max_idx < progresses[i]:
            result.append(lenth)
            max_idx = progresses[i]
            lenth = 1
    result.append(lenth)

    return result


print(solution(p0, s0))
print(solution(p1, s1))
