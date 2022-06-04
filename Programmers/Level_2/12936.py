import math


def solution(n, k):
    answer = []
    arr = [i + 1 for i in range(n)]
    k -= 1
    while arr:
        idx = k // math.factorial(n - 1)
        k = k % math.factorial(n - 1)
        n -= 1
        answer.append(arr.pop(idx))
    return answer


print(solution(3, 5))
