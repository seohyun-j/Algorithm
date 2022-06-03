import math


def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        if i < 2:
            answer.append(0)
            continue
        for j in range(2, int(math.sqrt(i)) + 1):
            mok = i // j
            if mok > 10 ** 7:
                continue
            if i % j == 0:
                answer.append(i // j)
                break
        else:
            answer.append(1)

    return answer


print(solution(1, 10))