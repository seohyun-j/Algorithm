from collections import deque


def chk_next(pos, board):
    n = len(board)

    next_arr = deque()

    pos = list(pos)
    y, x, ny, nx = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        py, px, pny, pnx = y + dy[i], x + dx[i], ny + dy[i], nx + dx[i]
        if not (0 <= py < n and 0 <= px < n and 0 <= pny < n and 0 <= pnx < n):
            continue
        if board[py][px] == 0 and board[pny][pnx] == 0:
            next_arr.append({(py, px), (pny, pnx)})

    if y == ny:
        for i in [-1, 1]:
            if 0 <= y + i < n and 0 <= ny + i < n:
                if board[y + i][x] == 0 and board[ny + i][nx] == 0:
                    next_arr.append({(y, x), (y + i, x)})
                    next_arr.append({(ny, nx), (ny + i, nx)})

    else:
        for i in [-1, 1]:
            if 0 <= x + i < n and 0 <= nx + i < n:
                if board[y][x + i] == 0 and board[ny][nx + i] == 0:
                    next_arr.append({(y, x), (y, x + i)})
                    next_arr.append({(ny, nx), (ny, nx + i)})

    return next_arr


def solution(board):
    n = len(board)

    queue = deque()
    queue.append([{(0, 0), (0, 1)}, 0])

    visited = [{(0, 0), (0, 1)}]

    while queue:
        pos, dis = queue.popleft()

        if (n - 1, n - 1) in pos:
            return dis

        for i in chk_next(pos, board):
            if i not in visited:
                queue.append((i, dis + 1))
                visited.append(i)

    return 0


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
