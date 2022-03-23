n0 = [3, 1, 2, 3]
n1 = [3, 3, 3, 2, 2, 4]
n2 = [3, 3, 3, 2, 2, 2]


def solution(nums):
    N = int(len(nums) / 2)
    nums = set(nums)
    if len(nums) >= N:
        return N
    else:
        return len(nums)


print(solution(n0))
print(solution(n1))
print(solution(n2))
