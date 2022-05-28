line0 = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
line1 = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
line2 = [[1, -1, 0], [2, -1, 0]]
line3 = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]

from itertools import combinations


def match(L1, L2):
    a, b, e = L1
    c, d, f = L2
    if a * d == b * c:
        return None
    x = (b * f - e * d) / (a * d - b * c)
    y = (e * c - a * f) / (a * d - b * c)
    if x == int(x) and y == int(y):
        return (int(x), int(y))


def solution(line):
    comb = list(combinations(line, 2))
    point = set()
    for p1, p2 in comb:
        pt = match(p1, p2)
        if pt:
            point.add(pt)

    px = [p[0] for p in point]
    py = [p[1] for p in point]
    max_x, min_x = max(px), min(px)
    max_y, min_y = max(py), min(py)

    arr = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    for x, y in point:
        arr[max_y - y][max_x - x] = '*'

    return [''.join(i) for i in arr]


print(solution(line0))
print(solution(line1))
print(solution(line2))
print(solution(line3))
