import numpy as np


def solution(rectangle, characterX, characterY, itemX, itemY):
    sizes = 51
    maps = np.zeros((sizes * 2, sizes * 2))

    for x1, y1, x2, y2 in rectangle:
        maps[y1 * 2 - 1:y2 * 2, x1 * 2 - 1:x2 * 2] = 1
    for x1, y1, x2, y2 in rectangle:
        maps[y1 * 2:y2 * 2 - 1, x1 * 2:x2 * 2 - 1] = 0

    x, y = characterX * 2 - 1, characterY * 2 - 1
    maps[y][x] = 0
    maps[itemY * 2 - 1][itemX * 2 - 1] = 2
    tmp, answer = 0, 0

    while True:
        tmp += 1
        if maps[y][x + 1] > 0:
            x += 1
        elif maps[y][x - 1] > 0:
            x -= 1
        elif maps[y - 1][x] > 0:
            y -= 1
        elif maps[y + 1][x] > 0:
            y += 1
        else:
            break

        if maps[y][x] == 2:
            answer = tmp

        maps[y][x] = 0

    return min(answer, tmp - answer) // 2


r0 = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
r1 = [[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]]
r2 = [[1, 1, 5, 7]]
r3 = [[2, 1, 7, 5], [6, 4, 10, 10]]
r4 = [[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]]

print(solution(r0, 1, 3, 7, 8))
print(solution(r1, 9, 7, 6, 1))
print(solution(r2, 1, 1, 4, 7))
print(solution(r3, 3, 1, 7, 10))
print(solution(r4, 1, 4, 6, 3))
