n0, n1, n2 = 9, 4, 7
wire0 = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
wire1 = [[1, 2], [2, 3], [3, 4]]
wire2 = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]

from collections import deque


def bfs(start, visited, arr):
    queue = deque([start])
    result = 1
    visited[start] = False
    while queue:
        now = queue.popleft()
        for i in arr[now]:
            if visited[i]:
                result += 1
                visited[i] = False
                queue.append(i)
    return result


def solution(n, wires):
    answer = n
    arr = [[] for _ in range(n + 1)]
    for i in wires:
        a, b = i
        arr[a].append(b)
        arr[b].append(a)

    for start, end in wires:
        visited = [True] * (n + 1)
        visited[end] = False
        result = bfs(start, visited, arr)
        answer = min(answer, abs(result - (n - result)))
        if answer == 0:
            break

    return answer


print(solution(n0, wire0))
print(solution(n1, wire1))
print(solution(n2, wire2))