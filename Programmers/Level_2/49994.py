d0 = "ULURRDLLU"
d1 = "LULLLLLLU"

def solution(dirs):
    dic = {'L': (0, -1), 'R': (0, 1), 'U': (1, 0), 'D': (-1, 0)}
    dx, dy = 0, 0
    load = set()
    for i in dirs:
        nx = dx + dic[i][1]
        ny = dy + dic[i][0]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            load.add((dy, dx, ny, nx))
            load.add((ny, nx, dy, dx))
            dy, dx = ny, nx

    return len(load)//2

print(solution(d0))
print(solution(d1))