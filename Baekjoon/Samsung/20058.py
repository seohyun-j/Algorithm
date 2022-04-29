import sys
input = sys.stdin.readline

n, q = map(int, input().split())
# maps = [list(map(int, input().split())) for _ in range(n**2-1)]
maps = [[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]]

arr = list(map(int, input().split()))

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

for i in arr:
    for j in range(0, len(maps), 2**i):
        p = [maps[k][j:j+2**i] for k in range(j, j+2**i)]
        p = rotate_90(p)
        print(p)
