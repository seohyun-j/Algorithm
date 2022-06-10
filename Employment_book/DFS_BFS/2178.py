from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]
visited[0][0] = True

queue = deque()
queue.append((0, 0, 1))

while queue:
    y, x, cnt = queue.popleft()

    if y == n - 1 and x == m - 1:
        print(cnt)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nd = cnt + 1
        if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = True
            queue.append((ny, nx, nd))
