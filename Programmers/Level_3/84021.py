from collections import deque
from collections import defaultdict


def solution(game_board, table):
    answer = 0
    n = len(table)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def BFS(maps, st_x, st_y, num):
        arr = [(0, 0)]

        queue = deque()
        queue.append((st_x, st_y, 0, 0))

        maps[st_y][st_x] = -1

        while queue:
            qx, qy, px, py = queue.popleft()

            for i in range(4):
                nx, ny = qx + dx[i], qy + dy[i]
                npx, npy = px + dx[i], py + dy[i]

                if 0 <= nx < n and 0 <= ny < n and maps[ny][nx] == num:
                    maps[ny][nx] = -1
                    queue.append((nx, ny, npx, npy))
                    arr.append((npx, npy))
        return arr

    board = defaultdict(int)
    for y in range(n):
        for x in range(n):
            if game_board[y][x] == 0:
                game_board[y][x] = -1
                board[tuple(BFS(game_board, x, y, 0))] += 1

    for _ in range(4):
        table = list(map(list, zip(*table[::-1])))
        copy_table = [row[:] for row in table]

        for y in range(n):
            for x in range(n):
                if copy_table[y][x] == 1:
                    copy_table[y][x] = -1
                    block = tuple(BFS(copy_table, x, y, 1))
                    if block in board:
                        board[block] -= 1
                        answer += len(block)
                        if not board[block]:
                            del board[block]
                        table = [row[:] for row in copy_table]
                else:
                    copy_table = [row[:] for row in table]

    return answer


# ---------------------------------------------------------------------------
# 아래는 다른 함수 풀이임 위의 함수가 훨씬 효율적임
def make_puzzle(i, j, table, chk):
    puzzle_x = []
    puzzle_y = []
    n = len(table)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((i, j))
    chk[i][j] = True

    while queue:
        x, y = queue.popleft()
        puzzle_x.append(y)
        puzzle_y.append(x)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if not chk[nx][ny] and table[nx][ny] == 1:
                queue.append((nx, ny))
                chk[nx][ny] = True

    min_x, max_x = min(puzzle_x), max(puzzle_x)
    min_y, max_y = min(puzzle_y), max(puzzle_y)

    len_x = max_x - min_x + 1
    len_y = max_y - min_y + 1
    trans = [[0] * len_x for _ in range(len_y)]

    for px, py in zip(puzzle_x, puzzle_y):
        x = px - min_x
        y = py - min_y
        trans[y][x] = 1

    return [trans, len(puzzle_x)]


def rotate(puzzle):
    return list(map(list, zip(*puzzle[::-1])))


def is_match(puzzle, board):
    n = len(board)
    len_y = len(puzzle)
    len_x = len(puzzle[0])

    for i in range(n - len_y + 1):
        for j in range(n - len_x + 1):
            match = True

            for x in range(len_y):
                for y in range(len_x):
                    board[x + i][y + j] += puzzle[x][y]
                    if board[x + i][y + j] != 1:
                        match = False

            if match:
                if find_empty(board, puzzle, i, j):
                    match = False

            if match:
                return True
            else:
                for x in range(len_y):
                    for y in range(len_x):
                        board[x + i][y + j] -= puzzle[x][y]

    return False


def find_empty(board, puzzle, i, j):
    n = len(board)
    len_y = len(puzzle)
    len_x = len(puzzle[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for x in range(len_y):
        for y in range(len_x):
            if puzzle[x][y] == 1:
                for k in range(4):
                    nx = x + i + dx[k]
                    ny = y + j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                        return True
    return False


def other_solution(game_board, table):
    answer = 0
    n = len(table)
    visited = [[False] * n for _ in range(n)]

    for a in range(n):
        for b in range(n):
            if table[a][b] == 1 and not visited[a][b]:
                val, key = make_puzzle(a, b, table, visited)
                for _ in range(4):
                    val = rotate(val)
                    if is_match(val, game_board):
                        answer += key
                        break

    return answer


'''
1. 퍼즐찾기(BFS)
2. 퍼즐 회전하기
3. 맞는 부분 있는지 확인하기 
'''

g0 = [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
      [0, 1, 1, 1, 0, 0]]
g1 = [[0, 0, 0], [1, 1, 0], [1, 1, 1]]
t0 = [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
      [0, 1, 0, 0, 0, 0]]
t1 = [[1, 1, 1], [1, 0, 0], [0, 0, 0]]

G0 = [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
      [0, 1, 1, 1, 0, 0]]
G1 = [[0, 0, 0], [1, 1, 0], [1, 1, 1]]
T0 = [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
      [0, 1, 0, 0, 0, 0]]
T1 = [[1, 1, 1], [1, 0, 0], [0, 0, 0]]

print(solution(g0, t0))
print(solution(g1, t1))
print(other_solution(G0, T0))
print(other_solution(G1, T1))
