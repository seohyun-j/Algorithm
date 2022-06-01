sk = "CBD"
sk_tree = ["BACDE", "CBADF", "AECB", "BDA"]

from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        queue = deque(list(skill))
        i = deque(i)
        result = True
        while i and queue:
            tmp = i.popleft()
            if tmp == queue[0]:
                queue.popleft()
            elif tmp in queue:
                result = False
                break

        if result:
            answer += 1

    return answer


print(solution(sk, sk_tree))
