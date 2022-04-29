import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

rate_left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
rate_right = [(x, -y, z) for x, y, z in rate_left]
rate_down = [(-y, x, z) for x, y, z in rate_left]
rate_up = [(y, x, z) for x, y, z in rate_left]

x, y = n // 2, n // 2
answer = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direct = {0: rate_left, 1: rate_down, 2: rate_right, 3: rate_up}
time = 0


def sand_count(x, y, d):
    global answer

    if y < 0:
        return

    total = 0
    for dx, dy, z in d:
        nx = x + dx
        ny = y + dy

        if z == 0:
            new_sand = arr[x][y] - total
        else:
            new_sand = int(arr[x][y] * z)
            total += new_sand

        if 0 <= nx < n and 0 <= ny < n:
            arr[nx][ny] += new_sand
        else:
            answer += new_sand


for i in range(2 * n - 1):
    key = i % 4
    print(key, time)
    if key == 0 or key == 2:
        time += 1
    for _ in range(time):
        nx = x + dx[key]
        ny = y + dy[key]
        sand_count(nx, ny, direct[key])
        x, y = nx, ny

print(answer)
