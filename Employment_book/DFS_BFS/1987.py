from collections import deque

r, c = map(int, input().split())
maps = [list(input()) for _ in range(r)]

answer = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
queue.append((0, 0, maps[0][0]))

visited = [[set() for _ in range(c)] for _ in range(r)]

while queue:
    y, x, s = queue.popleft()
    answer = max(answer, len(s))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < c and 0 <= ny < r and maps[ny][nx] not in s:
            ns = s + maps[ny][nx]
            if ns not in visited[ny][nx]:
                visited[ny][nx].add(ns)
                queue.append((ny, nx, ns))

print(answer)
