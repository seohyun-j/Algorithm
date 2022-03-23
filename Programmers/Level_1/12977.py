num0 = [1, 2, 3, 4]
num1 = [1, 2, 7, 6, 4]

import math
from itertools import combinations


def prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    nums = list(combinations(nums, 3))
    for i in nums:
        if prime(sum(i)):
            answer += 1
    return answer


print(solution(num0))
print(solution(num1))
