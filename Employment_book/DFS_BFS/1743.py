from collections import deque

n, m, k = map(int, input().split())

arr = [[''] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    arr[a-1][b-1] = '#'


answer = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(by, bx):
    queue = deque()
    queue.append((by, bx))
    visited[by][bx] = True
    cnt = 1

    while queue:
        y, x = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < m and 0 <= ny < n:
                if arr[ny][nx] == '#' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    cnt += 1

    return cnt


for i in range(n):
    for j in range(m):
        if arr[i][j] == '#' and not visited[i][j]:
            answer = max(answer, bfs(i, j))


print(answer)
