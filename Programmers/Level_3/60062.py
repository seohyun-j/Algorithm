from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    weak = weak + [w + n for w in weak]

    for st in range(length):
        for fr in permutations(dist):
            cnt = 1
            end_point = weak[st] + fr[cnt - 1]
            for i in range(st, st+length):
                if end_point < weak[i]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    end_point = weak[i] + fr[cnt - 1]
            if cnt == 1:
                return cnt
            answer = min(answer, cnt)
    return -1 if answer > len(dist) else answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
