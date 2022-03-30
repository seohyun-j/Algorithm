# 위의 조건을 만족하려면 해당 그래프의 깊이가 5임을 증명하면 됨

import sys

n, m = map(int, input().split())
arr1 = [[] for i in range(n)]
visited = [False] * n

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    arr1[a].append(b)
    arr1[b].append(a)

print(arr1)