from collections import deque


def solution(board):
    n = len(board)
    queue = deque()
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    visited[0][1] = 1

    queue.append([0, 0, 0, 1, 0])

    while queue:
        y, x, ny, nx, dis = queue.popleft()

        if ny == n - 1 and nx == n - 1:
            return dis

        if y == ny:
            # 옆으로 이동
            if 0 <= nx + 1 < n:
                if visited[ny][nx + 1] == 0 and board[ny][nx + 1] != 1:
                    queue.append((y, x + 1, ny, nx + 1, dis + 1))
                    visited[y][x + 1] = 1
                    visited[ny][nx + 1] = 1

            # 반시계방향으로 회전하여 이동
            if 0 <= y + 1 < n:
                if visited[y + 1][nx] == 0 and board[y + 1][nx] != 1 and board[y + 1][x] != 1:
                    queue.append((ny, nx, ny + 1, nx, dis + 1))
                    visited[y][nx] = 1
                    visited[ny + 1][nx] = 1

            # 시계방향으로 회전하여 이동
            if 0 <= y - 1 < n:
                if visited[y - 1][nx] == 0 and board[y - 1][nx] != 1 and board[y - 1][x] != 1:
                    queue.append((y - 1, nx, ny, nx, dis + 1))
                    visited[y - 1][nx] = 1
                    visited[ny][nx] = 1
        else:
            # 아래로 이동
            if 0 <= ny + 1 < n:
                if visited[ny + 1][nx] == 0 and board[ny + 1][nx] != 1:
                    queue.append((y + 1, x, ny + 1, nx, dis + 1))
                    visited[y + 1][x] = 1
                    visited[ny + 1][nx] = 1

            # 시계방향으로 회전하여 이동
            if 0 <= nx + 1 < n:
                if visited[ny][nx + 1] == 0 and board[ny][nx + 1] != 1 and board[y][nx + 1] != 1:
                    queue.append((ny, nx, ny, nx + 1, dis + 1))
                    visited[ny][nx] = 1
                    visited[ny][nx + 1] = 1

            # 반시계방향으로 회전하여 이동
            if 0 <= nx - 1 < n:
                if visited[ny][nx - 1] == 0 and board[ny][nx - 1] != 1 and board[y][nx - 1] != 1:
                    queue.append((ny, nx - 1, ny, nx, dis + 1))
                    visited[ny][nx] = 1
                    visited[ny][nx - 1] = 1

    return dis


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
