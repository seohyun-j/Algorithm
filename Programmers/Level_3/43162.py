c0 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
c1 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            BFS(n, computers, i, visited)
            answer += 1

    return answer


def BFS(n, computers, i, visited):
    queue = deque()
    queue.append(i)

    while queue:
        y = queue.popleft()
        visited[y] = True

        for x in range(n):
            if x != y and computers[y][x] and not visited[x]:
                queue.append(x)


print(solution(3, c0))
print(solution(3, c1))