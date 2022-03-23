a0 = [1, 2, 3, 4]
a1 = [-1, 0, 1]
b0 = [-3, -1, 0, 2]
b1 = [1, 0, -1]


def solution(a, b):
    answer = 0
    for p1, p2 in zip(a, b):
        answer += p1 * p2
    return answer


print(solution(a0, b0))
print(solution(a1, b1))
