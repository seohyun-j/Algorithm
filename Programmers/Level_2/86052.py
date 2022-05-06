g0 = ["SL", "LR"]
g1 = ["S"]
g2 = ["R", "R"]


def solution(grid):
    answer = []
    w, h = len(grid[0]), len(grid)
    S = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    R = {0: 3, 1: 2, 2: 0, 3: 1}
    L = {0: 2, 1: 3, 2: 1, 3: 0}

    cases = [[[1] * 4 for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            for i in range(4):
                if not cases[y][x][i]:
                    continue
                cnt = 0
                nx, ny, ni = x, y, i
                while True:
                    cases[ny][nx][ni] -= 1
                    cnt += 1
                    now = grid[ny][nx]
                    if now == 'L':
                        ni = L[ni]
                    elif now == 'R':
                        ni = R[ni]
                    nx, ny = (nx + S[ni][1]) % w, (ny + S[ni][0]) % h
                    if nx == x and ny == y and ni == i:
                        break
                answer.append(cnt)
    answer.sort()
    return answer



print(solution(g0))
print(solution(g1))
print(solution(g2))
