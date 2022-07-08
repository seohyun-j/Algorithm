from collections import deque


def solution(board, r, c):
    dic = {}

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] not in dic:
                    dic[board[i][j]] = []
                dic[board[i][j]].append((i, j))

    answer = len(dic.keys())*2

    def find_rc(board, dic, r, c):
        queue = deque()
        queue.append((r, c, 0, 5))

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        visited = [[False]*4 for _ in range(4)]
        visited[r][c] = True

        while queue:
            y, x, cnt, d = queue.popleft()

            if board[y][x] != 0:
                return y, x, cnt

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                


    for _ in range(answer//2):
        if board[r][c] != 0:
            p1, p2 = dic[board[r][c]]
            del dic[board[r][c]]
            y, x = p1 if (r, c) == p2 else p2
            if r != y:
                answer += 1
            if c != x:
                answer += 1
            board[r][c] = board[y][x] = 0
            r, c = y, x
        else:
            r, c = find_rc(board, dic, r, c)

    return answer


b0 = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
b1 = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
print(solution(b0, 1, 0))
print(solution(b1, 0, 1))
