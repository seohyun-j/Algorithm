from collections import deque


def solution(board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(board, dir):
        L = len(board)

        queue = deque()
        queue.append((0, 0, dir, 0))

        visited = [[int(1e9)]*L for _ in range(L)]

        while queue:
            x, y, d, val = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < L and 0 <= ny < L and board[nx][ny] != 1:
                    nv = val + 100 if d == i else val + 600

                    if visited[nx][ny] > nv:
                        visited[nx][ny] = nv
                        queue.append((nx, ny, i, nv))

        return visited[-1][-1]

    return min(bfs(board, 0), bfs(board, 2))


b0 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b1 = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0],
      [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
b2 = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
b3 = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1],
      [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]

print(solution(b0))
print(solution(b1))
print(solution(b2))
print(solution(b3))
