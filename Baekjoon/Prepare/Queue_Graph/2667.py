from collections import deque

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, x, y):
    limit = len(graph)
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= limit or ny < 0 or ny >= limit:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count


cnt = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt.append(bfs(arr, i, j))

cnt.sort()
print(len(cnt))

for i in range(len(cnt)):
    print(cnt[i])
