import sys
sys.setrecursionlimit(10000)
# 파이썬은 재귀제한이 있기 때문에 재귀 허용치가 넘어가면 런타임에러 따라서 위와 같이 입력

n, m = map(int, input().split())
arr = [[] for i in range(n+1)]
visited = [False]*(n+1)
answer = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()

def dfs(x):
    visited[x] = True
    for i in arr[x]:
        if not visited[i]:
            dfs(i)

for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        answer += 1


print(answer)