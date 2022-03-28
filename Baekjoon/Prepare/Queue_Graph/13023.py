

import sys

n, m = map(int, input().split())
arr1 = [[] for i in range(n)]
visited = [False] * n

# 그래프를 인접 리스트 방식으로 표현하였습니다.
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr1[a].append(b)
    arr1[b].append(a)

print(arr1)