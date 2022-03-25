s0 = [1, 2, 3, 9, 10, 12]
k0 = 7

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer


print(solution(s0, k0))
