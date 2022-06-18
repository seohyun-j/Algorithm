def rotate(key):
    return list(zip(*key[::-1]))


def attach(i, j, m, key, maps):
    for y in range(m):
        for x in range(m):
            maps[y + i][x + j] += key[y][x]


def detach(i, j, m, key, maps):
    for y in range(m):
        for x in range(m):
            maps[y + i][x + j] -= key[y][x]


def check(maps, n, m):
    for y in range(n):
        for x in range(n):
            if maps[m + y][m + x] != 1:
                return False
    return True


def solution(key, lock):
    n, m = len(lock), len(key)
    maps = [[0] * (2 * m + n) for _ in range(2 * m + n)]

    for i in range(n):
        for j in range(n):
            maps[m + i][m + j] = lock[i][j]

    rotate_key = key
    for _ in range(4):
        rotate_key = rotate(rotate_key)
        for i in range(1, n + m):
            for j in range(1, n + m):
                attach(i, j, m, rotate_key, maps)
                if check(maps, n, m):
                    return True
                detach(i, j, m, rotate_key, maps)

    return False


k0 = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
l0 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(k0, l0))
