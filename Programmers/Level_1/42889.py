n0 = 5
n1 = 4
s0 = [2, 1, 2, 6, 2, 4, 3, 3]
s1 = [4, 4, 4, 4, 4]


def solution(N, stages):
    answer = {}
    sum = len(stages)
    for i in range(1, N + 1):
        if sum == 0:
            answer[i] = 0
        else:
            key = stages.count(i)
            answer[i] = key / sum
            sum -= key
    return sorted(answer, key=lambda x: answer[x], reverse=True)


print(solution(n0, s0))
print(solution(n1, s1))
