n0, n1, n2, n3 = 5, 1, 9, 10
info0 = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
info1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
info2 = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
info3 = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]

from collections import deque


def bfs(n, info):
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0

    while q:
        focus, arrow = q.popleft()

        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap
                    res.clear()
                res.append(arrow)

        elif sum(arrow) > n:
            continue

        elif focus == 10:
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))

        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus] + 1
            q.append((focus + 1, tmp))
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus + 1, tmp2))
    return res


def solution(n, info):
    winList = bfs(n, info)

    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]


from itertools import combinations_with_replacement


def simulation_solution(n, info):
    ret = [-1] * 12
    for comb in combinations_with_replacement(range(11), n):
        arrow = [0] * 12
        score = 0

        for x in comb:
            arrow[x] += 1

        for i in range(11):
            if arrow[i] > info[i]:
                score += (10 - i)
            elif info[i] != 0:
                score -= (10 - i)

        if score <= 0:
            continue
        arrow[11] = score

        if arrow[::-1] > ret[::-1]:
            ret = arrow

    if ret[0] == -1:
        return [-1]

    return ret[:-1]


print(solution(n0, info0))
print(solution(n1, info1))
print(solution(n2, info2))
print(solution(n3, info3))

print(simulation_solution(n0, info0))
print(simulation_solution(n1, info1))
print(simulation_solution(n2, info2))
print(simulation_solution(n3, info3))

# BFS가 Simulation(중복조합)보다 효율적임