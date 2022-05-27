m0, n0 = 4, 5
m1, n1 = 6, 6
board0 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
board1 = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

def match(x, y, board, w, h):
    d = [(-1, 0), (0, 1), (-1, 1)]
    result = []
    for i in range(3):
        dx, dy = d[i]
        nx, ny = dx + x, dy + y

        if 0 <= nx < w and 0 <= y < h:
            print(nx, ny)
            if board[ny][nx] == board[y][x]:
                result.append((ny, nx))
    if len(result) == 3:
        result.append((y, x))
        print(result)
        return result
    return 0


def solution(m, n, board):
    answer = 0
    w, h = len(board[0]), len(board)
    board = list(map(list, zip(*board)))
    print(board)

    for y in range(h):
        for x in range(w):
            result = match(x, y, board, w, h)
    return answer


print(solution(m0, n0, board0))
print('-----------------------------------')
print(solution(m1, n1, board1))