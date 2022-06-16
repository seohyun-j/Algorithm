from collections import deque

n, m = map(int, input().split())

maps = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    maps[a - 1][b - 1] = maps[b - 1][a - 1] = True

answer = -1
total = 987654321
dist = [[0] * n for _ in range(n)]


def bfs(i, j):
    queue = deque()
    chk = [False] * n
    chk[i] = True
    queue.append((i, 0))

    while queue:
        now, dis = queue.popleft()
        if now == j:
            return dis

        for nxt in range(n):
            if maps[now][nxt] and not chk[nxt]:
                chk[nxt] = True
                queue.append((nxt, dis + 1))


for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j:
            if dist[i][j] == 0:
                dist[i][j] = dist[j][i] = bfs(i, j)
            cnt += dist[i][j]
    if total > cnt:
        answer = i
        total = cnt

print(answer + 1)
