from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
day = 0

queue = deque()

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append([nx, ny])
        print(arr)

bfs()
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))

print(day-1)