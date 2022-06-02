b0 = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
b1 = [[0, 0, 1, 1], [1, 1, 1, 1]]


def solution(board):
    answer = 0

    for y in range(1, len(board)):
        for x in range(1, len(board[0])):
            if board[y][x] == 1:
                board[y][x] = min(board[y][x - 1], board[y - 1][x], board[y - 1][x - 1]) + 1

    for i in range(len(board)):
        tmp = max(board[i])
        answer = max(answer, tmp)

    return answer ** 2


print(solution(b0))
print(solution(b1))
