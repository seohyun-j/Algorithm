o0 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
o1 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
o2 = ["XYZ", "XWY", "WXA"]
c0 = [2, 3, 4]
c1 = [2, 3, 5]
c2 = [2, 3, 4]

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        candidate = []
        for j in orders:
            for k in combinations(j, i):
                res = ''.join(sorted(k))
                candidate.append(res)
        sort_candidate = Counter(candidate).most_common()
        answer += [menu for menu, cnt in sort_candidate if cnt > 1 and cnt == sort_candidate[0][1]]
    return sorted(answer)


print(solution(o0, c0))
print(solution(o1, c1))
print(solution(o2, c2))
