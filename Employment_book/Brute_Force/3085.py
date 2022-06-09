n = int(input())
board = [list(input()) for _ in range(n)]
answer = 1


def search():
    global answer
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j - 1] == board[i][j]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1

    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if board[i - 1][j] == board[i][j]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1


for i in range(n):
    for j in range(n):
        if j + 1 < n:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            search()
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        if i + 1 < n:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            search()
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(answer)
