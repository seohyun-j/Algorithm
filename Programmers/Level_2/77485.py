r0 = 6
r1 = 3
r2 = 100
c0 = 6
c1 = 3
c2 = 97
q0 = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
q1 = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
q2 = [[1, 1, 100, 97]]


def solution(rows, columns, queries):
    answer = []
    arr = [[0 for col in range(columns)] for row in range(rows)]

    t = 1
    for row in range(rows):
        for col in range(columns):
            arr[row][col] = t
            t += 1

    for x1, y1, x2, y2 in queries:
        tmp = arr[x1 - 1][y1 - 1]
        mini = tmp

        # 왼쪽 세로
        for i in range(x1 - 1, x2 - 1):
            val = arr[i + 1][y1 - 1]
            arr[i][y1 - 1] = val
            mini = min(mini, val)

        # 하단 가로
        for i in range(y1 - 1, y2 - 1):
            val = arr[x2 - 1][i + 1]
            arr[x2 - 1][i] = val
            mini = min(mini, val)

        # 오른쪽 세로
        for i in range(x2 - 1, x1 - 1, -1):
            val = arr[i - 1][y2 - 1]
            arr[i][y2 - 1] = val
            mini = min(mini, val)

        # 상단 가로
        for i in range(y2 - 1, y1 - 1, -1):
            val = arr[x1 - 1][i - 1]
            arr[x1 - 1][i] = val
            mini = min(mini, val)

        arr[x1 - 1][y1] = tmp
        answer.append(mini)

    return answer



print(solution(r0, c0, q0))
print(solution(r1, c1, q1))
print(solution(r2, c2, q2))
