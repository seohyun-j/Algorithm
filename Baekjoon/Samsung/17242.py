from collections import deque
from itertools import permutations
from copy import deepcopy
import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = math.inf
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 2:
            virus.append((i, j, 0))

virus = list(permutations(virus, 3))


def check(maps):
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0:
                return -1
    return 0


def bfs(v, maps):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    maps = deepcopy(maps)
    queue = deque()

    queue.extend(v)
    last_change = 0

    while queue:
        cy, cx, cnt = queue.popleft()
        visited[cy][cx] = 1
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and maps[ny][nx] != 1:
                visited[ny][nx] = 1
                if maps[ny][nx] == 0:
                    maps[ny][nx] = 2
                    last_change = cnt + 1
                queue.append((ny, nx, cnt + 1))

    chk = check(maps)
    if chk == 0:
        return last_change
    else:
        return -1


for val in virus:
    result = bfs(val, arr)
    if result != -1:
        answer = min(answer, result)

if answer == math.inf:
    print(-1)
else:
    print(answer)
