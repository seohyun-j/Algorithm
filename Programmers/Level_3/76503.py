from collections import deque


def bfs(a, edges):
    graph = {}

    for u, v in edges:
        if u not in graph:
            graph[u] = deque()
        if v not in graph:
            graph[v] = deque()

        graph[u].append(v)
        graph[v].append(u)

    root = min(graph.keys(), key=lambda x: len(graph[x]))

    visited = [False] * len(a)
    visited[root] = True
    visited[graph[root][0]] = True

    queue = deque()
    queue.append((root, graph[root].popleft()))
    path = []

    while queue:
        top, bottom = queue.popleft()
        path.append((top, bottom))

        for i in graph[bottom]:
            if not visited[i]:
                queue.append((bottom, i))
                visited[i] = True

    return root, path[::-1]


def solution(a, edges):
    answer = 0

    if sum(a) != 0:
        return -1

    root, path = bfs(a, edges)

    for nex, pre in path:
        val = a[pre]
        answer += abs(val)
        a[pre] += -1 * val
        a[nex] += val

    return answer


# DFS 풀이방법
# 이 문제에선 BFS보다 DFS가 훨씬 빠름
import sys

sys.setrecursionlimit(300000)


def dfs(x, a, board):
    global visited
    global answer

    now = a[x]
    visited[x] = 1

    for i in board[x]:
        if visited[i] == 0:
            now += dfs(i, a, board)

    answer += abs(now)

    return now


def dfs_solution(a, edges):
    global visited
    global answer

    if sum(a) != 0:
        return -1

    answer = 0
    length = len(a)
    board = [[] for _ in range(length)]
    visited = [0] * length

    for i, j in edges:
        board[i].append(j)
        board[j].append(i)

    dfs(0, a, board)

    return answer


a0 = [-5, 0, 2, 1, 2]
a1 = [0, 1, 0]
e0 = [[0, 1], [3, 4], [2, 3], [0, 3]]
e1 = [[0, 1], [1, 2]]

print(solution(a0, e0))
print(solution(a1, e1))
print(dfs_solution(a0, e0))
print(dfs_solution(a1, e1))
