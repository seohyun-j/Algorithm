from collections import deque


def other_solution(board, r, c):
    dic = {}

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                if board[i][j] not in dic:
                    dic[board[i][j]] = []
                dic[board[i][j]].append((i, j))

    answer = len(dic.keys()) * 2

    def find_rc(maps, by, bx):
        queue = deque()
        queue.append((by, bx, 0, 5))

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        visited = [[False] * 4 for _ in range(4)]
        visited[by][bx] = True

        key = 100

        while queue:
            y, x, cnt, d = queue.popleft()

            if maps[y][x] != 0:
                if key > cnt:
                    key_x, key_y = x, y
                    key = cnt

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < 4 and 0 <= ny < 4):
                    continue

                if visited[ny][nx]:
                    continue

                visited[ny][nx] = True
                tmp = cnt + 1 if d != i else cnt
                queue.append((ny, nx, tmp, i))
        return key_y, key_x, key

    for _ in range(answer // 2):
        if board[r][c] == 0:
            r, c, cnt = find_rc(board, r, c)
            answer += cnt

        p1, p2 = dic[board[r][c]]
        y, x = p1 if (r, c) == p2 else p2
        if r != y:
            answer += 1
        if c != x:
            answer += 1
        board[r][c] = board[y][x] = 0
        r, c = y, x

    return answer


from itertools import permutations
from collections import deque


def ctrl(board, x0, y0, dx, dy):
    for i in range(1, 4):
        if 0 <= (x1 := x0 + dx * i) < 4 and 0 <= (y1 := y0 + dy * i) < 4:
            if board[x1][y1] > 0:
                return (x1, y1)
            l = i
    return (x0 + dx * l, y0 + dy * l)


def move(board, xy0, xy1):
    visited = [[6] * 4 for _ in range(4)]
    queue = deque([(xy0, 0)])

    while queue:
        [x, y], dis = queue.popleft()
        if dis < visited[x][y]:
            visited[x][y] = dis
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < 4 and 0 <= y + dy < 4:
                    queue.append(((x + dx, y + dy), dis + 1))
                    queue.append((ctrl(board, x, y, dx, dy), dis + 1))
    return visited[xy1[0]][xy0[1]]


def solution(board, r, c):
    answer = 100
    dic = {}

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                if board[i][j] not in dic:
                    dic[board[i][j]] = []
                dic[board[i][j]].append((i, j))

    # filter(함수, 리스트)는 리스트에서 함수의 조건에 맞는 값을 반환하는 함수임
    # := 연산자는 할당과 연산을 동시에 진행할 수 있음

    for i in permutations(dic.values()):
        cnt = 0
        arr = [(r, c)]
        maps = [[v for v in w] for w in board]

        for k1, k2 in i:
            tmp = [(move(maps, xy, k1) + move(maps, k1, k2), k2) for xy in arr] \
                  + [(move(maps, xy, k2) + move(maps, k2, k1), k1) for xy in arr]
            print(tmp)
            maps[k1[0]][k2[1]] = maps[k2[0]][k1[0]] = 0
            cnt += 2 + (mvn := min(tmp)[0])
            arr = [xy for m, xy in arr if m == mvn]
        answer = min(answer, cnt)
    return answer


b0 = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
b1 = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
print(solution(b0, 1, 0))
print(solution(b1, 0, 1))
