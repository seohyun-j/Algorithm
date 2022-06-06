import sys

sys.setrecursionlimit(60000)


def solution(n):
    cache = [-1 for _ in range(60001)]

    def dp(n):
        if cache[n] != -1:
            return cache[n]
        if n == 0 or n == 1:
            return 1
        cache[n] = (dp(n - 1) + dp(n - 2)) % 1000000007
        return cache[n]

    return dp(n)


print(solution(4))
