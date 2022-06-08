import heapq
hq = []
n = int(input())

for _ in range(n):
    for i in map(int, input().split()):
        if len(hq) >= n:
            heapq.heappushpop(hq, i)
        else:
            heapq.heappush(hq, i)

print(heapq.heappop(hq))