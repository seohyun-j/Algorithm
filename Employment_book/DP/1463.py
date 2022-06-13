# Top-down 방식
import sys

sys.setrecursionlimit(10 ** 6)
INF = 987654321
n = int(input())
memo = [INF] * (n + 1)
memo[1] = 0


def dp(x):
    if memo[x] != INF:
        return memo[x]

    if x % 6 == 0:
        memo[x] = min(dp(x // 3), dp(x // 2)) + 1
    elif x % 3 == 0:
        memo[x] = min(dp(x // 3), dp(x - 1)) + 1
    elif x % 2 == 0:
        memo[x] = min(dp(x // 2), dp(x - 1)) + 1
    else:
        memo[x] = dp(x - 1) + 1

    return memo[x]


print(dp(n))

# Bottom-Up 방식
cache = [INF] * (n + 1)
cache[1] = 0

for i in range(2, n + 1):
    if i % 6 == 0:
        cache[i] = min(cache[i // 3], cache[i // 2]) + 1
    elif i % 3 == 0:
        cache[i] = min(cache[i // 3], cache[i - 1]) + 1
    elif i % 2 == 0:
        cache[i] = min(cache[i // 2], cache[i - 1]) + 1
    else:
        cache[i] = cache[i - 1] + 1

print(cache[n])

# BFS방식
from collections import deque

queue = deque()
queue.append((n, 0))
chk = [False] * (n + 1)
chk[n] = True
while queue:
    x, d = queue.popleft()

    if x == 1:
        print(d)
        break

    if x % 3 == 0 and not chk[x // 3]:
        queue.append((x // 3, d + 1))
        chk[x // 3] = True

    if x % 2 == 0 and not chk[x // 2]:
        queue.append((x // 2, d + 1))
        chk[x // 2] = True

    if not chk[x - 1]:
        queue.append((x - 1, d + 1))
        chk[x - 1] = True
