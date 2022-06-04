a0, b0 = [1, 4, 2], [5, 4, 4]
a1, b1 = [1, 2], [3, 4]


def solution(A, B):
    answer = 0

    A = sorted(A)
    B = sorted(B, reverse=True)
    for i, j in zip(A, B):
        answer += (i * j)

    return answer


print(solution(a0, b0))
print(solution(a1, b1))
