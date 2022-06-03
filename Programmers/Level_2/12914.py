n0, n1 = 4, 3

import math


def solution(n):
    answer = 1
    lmt = n // 2
    for i in range(1, lmt + 1):
        cnt1 = n - 2 * i
        if cnt1 == 0:
            answer += 1
        else:
            k = math.factorial(cnt1 + i) // (math.factorial(i) * math.factorial(cnt1))
            answer += k

    return answer % 1234567


# 아래 방법은 재귀함수를 이용한 방법인데, 시간초과에서 걸려버림
def other_solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return solution(n - 1) + solution(n - 2)


print(solution(n0))
print(solution(n1))
