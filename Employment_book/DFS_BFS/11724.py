import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[False] * n for _ in range(n)]
answer = 0
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = True
    arr[b - 1][a - 1] = True


def dfs(i):
    for j in range(n):
        if arr[i][j] and not visited[j]:
            visited[j] = True
            dfs(j)


for i in range(n):
    if not visited[i]:
        answer += 1
        visited[i] = True
        dfs(i)

print(answer)
