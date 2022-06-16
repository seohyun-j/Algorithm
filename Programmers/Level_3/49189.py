n0 = 6
v0 = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

from collections import deque


def solution(n, edge):
    answer = 0
    maps = [[] for _ in range(n)]
    chk = [-1] * n

    queue = deque()
    queue.append((0, 0))

    for e in edge:
        a, b = e
        maps[a - 1].append(b - 1)
        maps[b - 1].append(a - 1)

    while queue:
        now, dis = queue.popleft()

        if chk[now] == -1:
            chk[now] = dis
            for nxt in maps[now]:
                queue.append((nxt, dis + 1))

    result = max(chk)

    for i in chk:
        if i == result:
            answer += 1

    return answer


print(solution(n0, v0))
