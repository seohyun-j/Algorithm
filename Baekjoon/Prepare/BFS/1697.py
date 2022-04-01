from collections import deque

n, k = map(int, input().split())
MAX = 100000
dist = [0]*(MAX+1)

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break

        for j in (x-1, x+1, x*2):
            if 0 <= j <= MAX and not dist[j]:
                dist[j] = dist[x] + 1
                queue.append(j)

bfs()
