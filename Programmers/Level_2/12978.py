n0 = 5
n1 = 6
r0 = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
r1 = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
k0 = 3
k1 = 4

import heapq


def solution(n, road, k):
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(start=1)
    return len([d for d in distance if d <= k])


print(solution(n0, r0, k0))
print(solution(n1, r1, k1))