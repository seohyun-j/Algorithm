import heapq

for _ in range(int(input())):
    m = int(input())
    arr = []
    for _ in range(m // 10 + 1):
        arr.extend(list(map(int, input().split())))

    answer = []
    max_hq = []
    min_hq = []


    def priority_queue(n):
        if max_hq and n >= -max_hq[0]:
            heapq.heappush(min_hq, n)
        else:
            heapq.heappush(max_hq, -n)

        if len(max_hq) > len(min_hq) + 2:
            heapq.heappush(min_hq, -heapq.heappop(max_hq))
        elif len(max_hq) < len(min_hq):
            heapq.heappush(max_hq, -heapq.heappop(min_hq))


    for idx, val in enumerate(arr):
        priority_queue(val)

        if idx % 2 == 0:
            answer.append(-max_hq[0])

    print((m + 1) // 2)
    for i in range(len(answer) // 10 + 1):
        print(*answer[i * 10: (i + 1) * 10])
