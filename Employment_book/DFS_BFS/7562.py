from collections import deque

for _ in range(int(input())):
    n = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())

    dy = [2, 2, -2, -2, 1, 1, -1, -1]
    dx = [1, -1, 1, -1, 2, -2, 2, -2]

    arr = [[False] * n for _ in range(n)]
    arr[sy][sx] = True

    queue = deque()
    queue.append((sy, sx, 0))

    while queue:
        y, x, cnt = queue.popleft()
        nd = cnt + 1

        if y == ey and x == ex:
            print(cnt)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not arr[ny][nx]:
                arr[ny][nx] = True
                queue.append((ny, nx, nd))
