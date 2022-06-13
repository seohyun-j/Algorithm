import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())
cache = [0] * (n + 1)


def dp(x):
    if cache[x]:
        return cache[x]

    cache[x] = x if x <= 2 else (dp(x - 1) + dp(x - 2)) % 10007

    return cache[x]


print(dp(n))
