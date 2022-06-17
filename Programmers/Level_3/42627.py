import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    hq = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(hq, (j[1], j[0]))

        if len(hq) > 0:
            cur = heapq.heappop(hq)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1

        else:
            now += 1

    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))
