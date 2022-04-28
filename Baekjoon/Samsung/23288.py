from collections import deque

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dice = [2, 4, 1, 3, 5, 6]
d = 0
score = 0
vector = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x, y = 0, 0


def change_dice(dice, d):
    if d == 0:
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
    elif d == 1:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
    elif d == 2:
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
    elif d == 3:
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]


def check(a, b):
    if 0 <= a < n and 0 <= b < m:
        return False
    return True


def bfs(a, b):
    cnt = 1
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + vector[i][0], y + vector[i][1]
            if check(nx, ny):
                continue
            if arr[x][y] == arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append([nx, ny])
                cnt += 1
    return cnt


def dice_move(a, b, d):
    na, nb = a + vector[d][0], b + vector[d][1]
    if check(na, nb):
        nd = (d + 2) % 4
        na, nb = a + vector[nd][0], b + vector[nd][1]
        return [na, nb, nd]
    return [na, nb, d]


for _ in range(k):
    x, y, d = dice_move(x, y, d)
    C = bfs(x, y)
    score += arr[x][y] * C
    A, B = dice[5], arr[x][y]
    if A > B:
        d = (d + 1) % 4
    elif A < B:
        d = d - 1
        if d == -1:
            d = 3
    elif A == B:
        pass

print(score)
