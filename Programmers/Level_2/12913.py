l = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]


def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
    return max(land[-1])


def false_solution(land):
    answer = 0
    col = 5
    for i in land:
        tmp = sorted(i, reverse=True)
        max_tmp = i.index(tmp[0])
        if col == max_tmp:
            answer += tmp[1]
            col = i.index(tmp[1])
        else:
            answer += tmp[0]
            col = max_tmp
    return answer


print(solution(l))
