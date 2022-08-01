def solution(n, stations, w):
    answer = 0
    visited = [False for _ in range(n)]

    for i in stations:
        for j in range(i - w - 1, i + w):
            if 0 < j < n:
                visited[j] = True

    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
