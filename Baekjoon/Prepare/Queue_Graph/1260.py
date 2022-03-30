import sys
from collections import deque

n, m, v = map(int, input().split())
arr = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    arr.sort()

d_visited = [False for _ in range(n + 1)]


def dfs(x):
    d_visited[x] = True
    print(x, end=' ')
    for y in arr[x]:
        if not d_visited[y]:
            dfs(y)

def bfs():
    queue = deque([v])
    b_visited = [False for _ in range(n+1)]
    b_visited[v] = True
    while queue:
        k = queue.popleft()
        print(k, end=' ')
        for i in arr[k]:
            if not b_visited[i]:
                b_visited[i] = True
                queue.append(i)

dfs(v)
print()
bfs()
print()

