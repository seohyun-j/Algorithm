n0, l0, r0 = 3, 2, 5
n1, l1, r1 = 4, 7, 14


def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n
        b = i % n
        answer.append(max(a, b) + 1)
    return answer


print(solution(n0, l0, r0))
print(solution(n1, l1, r1))
