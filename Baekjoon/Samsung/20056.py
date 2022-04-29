import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
maps = [[[] for _ in range(n)] for _ in range(n)]
try_arr = []

direct = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(k):
    while arr:
        x, y, m, s, d = arr.pop()
        nx = (x + direct[d][0]*s - 1) % n
        ny = (y + direct[d][1]*s - 1) % n
        maps[nx][ny].append([m, s, d])

    for i in range(n):
        for j in range(n):
            if len(maps[i][j]) > 1:
                tm, ts, tl, odd, even = 0, 0, len(maps[i][j]), 0, 0
                while maps[i][j]:
                    nm, ns, nd = maps[i][j].pop()
                    tm += nm
                    ts += ns
                    if nd % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                if odd == tl or even == tl:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if tm//5:
                    for val in nd:
                        arr.append([i, j, tm//5, ts//tl, val])

            if len(maps[i][j]) == 1:
                arr.append([i, j] + maps[i][j].pop())

print(sum([i[2] for i in arr]))
