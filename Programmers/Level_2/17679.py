m0, n0 = 4, 5
m1, n1 = 6, 6
board0 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
board1 = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


def match(m, n, board):
    result = set()

    for y in range(0, n - 1):
        for x in range(0, m - 1):
            if board[y][x] == board[y + 1][x + 1] == board[y][x + 1] == board[y + 1][x]:
                result |= {(y, x), (y + 1, x), (y, x + 1), (y + 1, x + 1)}

    for i, j in result:
        board[i][j] = ''
    print(len(result))
    board = [list(''.join(i) + ' ' * (m - len(''.join(i)))) for i in board]

    return board, 1


def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    for _ in range(3):
        result = set()

        for y in range(0, n - 1):
            for x in range(0, m - 1):
                if board[y][x] == board[y + 1][x + 1] == board[y][x + 1] == board[y + 1][x]:
                    result |= {(y, x), (y + 1, x), (y, x + 1), (y + 1, x + 1)}
        print(result)
        for i, j in result:
            board[i][j] = ''

        board = [list(''.join(i) + ' ' * (m - len(''.join(i)))) for i in board]
    return board


print(solution(m0, n0, board0))
print('-----------------------------------')
print(solution(m1, n1, board1))
