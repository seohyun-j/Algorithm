n0 = [2, 1, 3, 4, 1]
n1 = [5, 0, 2, 7]

from itertools import combinations


def solution(numbers):
    arr = set(sum(i) for i in list(combinations(numbers, 2)))
    return sorted(arr)


print(solution(n0))
print(solution(n1))
