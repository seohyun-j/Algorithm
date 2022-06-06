import heapq, sys

input = sys.stdin.readline

hq = []
for _ in range(int(input())):
    key = int(input())
    if key == 0:
        print(heapq.heappop(hq)[1] if len(hq) else 0)
    else:
        heapq.heappush(hq, (abs(key), key))