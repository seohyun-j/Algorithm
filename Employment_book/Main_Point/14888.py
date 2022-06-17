# BFS 이용방식으로 시간과 메모리 측면에서 훨씬 절약됨
def bfs():
    from collections import deque

    n = int(input())
    arr = list(map(int, input().split()))
    ops = list(map(int, input().split()))

    max_cnt = -1_000_000_001
    min_cnt = 1_000_000_001

    queue = deque()
    queue.append((arr[0], 1, ops[0], ops[1], ops[2], ops[3]))

    while queue:
        res, i, plus, minus, multi, div = queue.popleft()

        if i == n:
            max_cnt = max(max_cnt, res)
            min_cnt = min(min_cnt, res)
            continue

        if plus:
            queue.append((res + arr[i], i + 1, plus - 1, minus, multi, div))

        if minus:
            queue.append((res - arr[i], i + 1, plus, minus - 1, multi, div))

        if multi:
            queue.append((res * arr[i], i + 1, plus, minus, multi - 1, div))

        if div:
            nxt_res = res // arr[i] if res >= 0 else -(-res // arr[i])
            queue.append((nxt_res, i + 1, plus, minus, multi, div - 1))

    print(max_cnt)
    print(min_cnt)

    return


# 중복순열을 이용한 방식으로 permutations을 이용하여 순열을 구한 후 set을 사용하여 중복 제거
def permu():
    from itertools import permutations

    n = int(input())
    arr = list(map(int, input().split()))
    ops = []

    for idx, val in enumerate(list(map(int, input().split()))):
        ops += [idx] * val

    max_cnt = -1_000_000_001
    min_cnt = 1_000_000_001

    for per in set(permutations(ops, n - 1)):
        res = arr[0]
        for i, op in enumerate(per):
            if op == 0:
                res += arr[i + 1]
            elif op == 1:
                res -= arr[i + 1]
            elif op == 2:
                res *= arr[i + 1]
            else:
                if res >= 0:
                    res //= arr[i + 1]
                else:
                    res = -(-res // arr[i + 1])

        max_cnt = max(max_cnt, res)
        min_cnt = min(min_cnt, res)

    print(max_cnt)
    print(min_cnt)

    return
