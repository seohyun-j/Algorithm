bd = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
mv = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    answer = []
    count = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                answer.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
        if len(answer) > 1 and answer[-1] == answer[-2]:
            del answer[-2]
            del answer[-1]
            count += 2
    return count


print(solution(bd, mv))
