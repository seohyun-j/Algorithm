import sys
from collections import deque

input = sys.stdin.readline

n, q = map(int, input().split())
N = 2 ** n
# maps = [list(map(int, input().split())) for _ in range(N)]
maps = [[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]]

new_maps = [[0] * N for _ in range(N)]
arr = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_ice_bfs(maps, N):
    used = [[False] * N for _ in range(N)]
    ice_sum = 0
    max_area_count = 0
    for y in range(N):
        for x in range(N):
            area_count = 0
            if used[y][x] or maps[y][x] == 0:
                continue
            # BFS를 이용하여 얼음 덩어리 조사
            q = deque()
            q.append((y, x))
            used[y][x] = True

            while q:
                sy, sx = q.popleft()
                ice_sum += maps[sy][sx]  # 얼음 합 추가
                area_count += 1  # 얼음 카운트 추가

                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dx[d]
                    if nx < 0 or ny < 0 or nx >= N or ny >= N or used[ny][nx]:
                        continue
                    if maps[ny][nx] != 0:
                        used[ny][nx] = True
                        q.append((ny, nx))

            max_area_count = max(max_area_count, area_count)  # 최대 얼음 덩어리 크기 파악

    print(ice_sum)
    print(max_area_count)


for i in arr:
    L = 2 ** i
    for y in range(0, N, L):  # 격자 시작 좌표 y축
        for x in range(0, N, L):  # 격자 시작 좌표 x축
            for k in range(L):  # 열 인덱스
                for j in range(L):  # 행 인덱스
                    new_maps[y + j][x + L - k - 1] = maps[y + k][x + j]
    maps = new_maps

    for x in range(N):
        for y in range(N):
            cnt = 0
            if maps[x][y] == 0:
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] > 0:
                    cnt += 1
            if cnt < 3:
                maps[x][y] -= 1

check_ice_bfs(maps, N)

