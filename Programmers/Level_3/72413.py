# 플로이드-워셜 알고리즘

def solution(n, s, a, b, fares):
    answer = 200000001
    maps = [[answer] * (n + 1) for _ in range(n + 1)]

    for p1, p2, dis in fares:
        maps[p1][p2] = maps[p2][p1] = dis

    def floyd_warshall():
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(i, n + 1):
                    if i == j:
                        maps[i][j] = 0
                    else:
                        chk = min(maps[i][j], maps[i][k] + maps[k][j])
                        maps[i][j] = maps[j][i] = chk

    floyd_warshall()

    for i in range(1, n + 1):
        tmp = maps[s][i] + maps[i][b] + maps[i][a]
        answer = min(answer, tmp)

    return answer


# 다익스트라 알고리즘 -> 플로이드-워셜 알고리즘보다 시간측면에서 단축됨

import heapq


def other_solution(n, s, a, b, fares):
    answer = 200000001
    maps = [[] for _ in range(n + 1)]
    dist = [[]]

    for p1, p2, dis in fares:
        maps[p1].append((p2, dis))
        maps[p2].append((p1, dis))

    def dijkstra(start):
        res = [float('inf') for _ in range(n + 1)]
        res[start] = 0
        heap = []
        heapq.heappush(heap, (res[start], start))

        while heap:
            distance, x = heapq.heappop(heap)
            for nx, nd in maps[x]:
                if res[nx] > distance + nd:
                    res[nx] = distance + nd
                    heapq.heappush(heap, (res[nx], nx))

        return res

    for i in range(1, n + 1):
        dist.append(dijkstra(i))

    for i in range(1, n + 1):
        tmp = dist[i][s] + dist[i][a] + dist[i][b]
        answer = min(answer, tmp)

    return answer


f0 = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
f1 = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
f2 = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]

print('floyd-warshall algorithm')
print(solution(6, 4, 6, 2, f0))
print(solution(7, 3, 4, 1, f1))
print(solution(6, 4, 5, 6, f2))
print('dijkstra algorithm')
print(other_solution(6, 4, 6, 2, f0))
print(other_solution(7, 3, 4, 1, f1))
print(other_solution(6, 4, 5, 6, f2))
