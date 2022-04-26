from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(input()))
    for j in range(m):
        if arr[i][j] == 'R': # 빨간구슬 위치
            rx, ry = i, j
        if arr[i][j] == 'B': # 파란구슬 위치
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by))
    visited = [(rx, ry, bx, by)] # 방문 여부를 판단하기 위한 리스트
    count = 0

    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()
            if count > 10: # 움직인 횟수가 10회를 초과하면 -1을 출력
                print(-1)
                return
            if arr[rx][ry] == 'O': # 현재 빨간 구슬의 위치가 구멍이라면 count 출력
                print(count)
                return
            for i in range(4): # 4방향으로 탐색
                nrx, nry = rx, ry
                while True: # 벽 또는 구멍일 때까지 빨간 구슬 움직임
                    nrx += dx[i]
                    nry += dy[i]
                    if arr[nrx][nry] == '#': # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if arr[nrx][nry] == 'O':
                        break

                nbx, nby = bx, by
                while True: # 벽 또는 구멍일 때까지 파란 구슬 움직임
                    nbx += dx[i]
                    nby += dy[i]
                    if arr[nbx][nby] == '#': # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if arr[nbx][nby] == 'O':
                        break

                if arr[nbx][nby] == 'O': # 파란 구슬이 먼저 구멍에 들어가거나 동시에 들어가면 안되므로 무시
                    continue

                if nrx == nbx and nry == nby: # 두 구슬의 위치가 같다면
                    # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 뒤로 이동
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                # 방문한 적이 없는 위치라면 새로 큐에 추가 후 방문처리
                if (nrx, nry, nbx, nby) not in visited:
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1) # 10회를 초과하지 않았지만 구멍에 들어가지 못하는 경우 -1 return


bfs(rx, ry, bx, by)
