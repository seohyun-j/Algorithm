bd = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
mv = [1, 5, 3, 5, 1, 2, 1, 4]


# mysolution은 두번째 풀이인데 정확성 테스트의 효율성이 더 좋았음

def mysolution(board, moves):
    answer = 0
    board = list(zip(*board))
    board = [list(i) for i in board]
    arr = []
    for i in moves:
        for j in range(len(board[i - 1])):
            if board[i - 1][j] != 0:
                if len(arr) != 0 and arr[-1] == board[i - 1][j]:
                    answer += 2
                    arr.pop()
                else:
                    arr.append(board[i - 1][j])
                board[i - 1][j] = 0
                break
            else:
                pass
    return answer


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
