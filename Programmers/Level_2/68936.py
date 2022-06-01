arr0 = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
arr1 = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]


def solution(arr):
    answer = [0, 0]
    length = len(arr)

    def half_match(x, y, L):
        init = arr[y][x]
        for i in range(y, y + L):
            for j in range(x, x + L):
                if arr[i][j] != init:
                    L = L // 2
                    half_match(x, y, L)
                    half_match(x, y + L, L)
                    half_match(x + L, y, L)
                    half_match(x + L, y + L, L)
                    return
        answer[init] += 1

    half_match(0, 0, length)
    return answer


print(solution(arr0))
print(solution(arr1))