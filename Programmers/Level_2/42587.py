p0 = [2, 1, 3, 2]
p1 = [1, 1, 9, 1, 1, 1]
l0 = 2
l1 = 0

from collections import deque


def solution(priorities, location):
    answer = 0
    d = deque([(v, i) for i, v in enumerate(priorities)])
    while len(d):
        item = d.popleft()
        if max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer


print(solution(p0, l0))
print(solution(p1, l1))
