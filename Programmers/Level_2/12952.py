def solution(n):
    answer = 0

    def dfs(queens, nq):
        nonlocal answer
        if nq in queens:
            return

        for row, col in enumerate(queens):
            h = len(queens) - row
            if nq == col + h or nq == col - h:
                return

        queens.append(nq)

        if len(queens) == n:
            answer += 1
            return

        for nq in range(n):
            dfs(queens, nq)

    for nq in range(n):
        queens = []
        dfs(queens, nq)

    return answer


print(solution(4))