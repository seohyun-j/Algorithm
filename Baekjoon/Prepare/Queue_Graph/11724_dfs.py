import sys

sys.setrecursionlimit(10000)
# 파이썬은 재귀제한이 있기 때문에 재귀 허용치가 넘어가면 런타임에러 따라서 위와 같이 입력

n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()

d_visited = [False] * (n + 1)
d_answer = 0


def dfs(x):
    d_visited[x] = True
    for i in arr[x]:
        if not d_visited[i]:
            dfs(i)


for j in range(1, n + 1):
    if not d_visited[j]:
        dfs(j)
        d_answer += 1



print(d_answer)

