m0, n0 = 4, 5
m1, n1 = 6, 6
board0 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
board1 = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    while True:
        result = set()

        for y in range(0, n - 1):
            for x in range(0, m - 1):
                if board[y][x] != ' ':
                    if board[y][x] == board[y + 1][x + 1] == board[y][x + 1] == board[y + 1][x]:
                        result |= {(y, x), (y + 1, x), (y, x + 1), (y + 1, x + 1)}
        answer += len(result)
        if not result:
            break

        for i, j in result:
            board[i][j] = ''

        board = [list(' ' * (m - len(''.join(i))) + ''.join(i)) for i in board]

    return answer


print(solution(m0, n0, board0))
print(solution(m1, n1, board1))
