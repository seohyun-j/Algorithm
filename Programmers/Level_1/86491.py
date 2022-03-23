s0 = [[60, 50], [30, 70], [60, 30], [80, 40]]
s1 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
s2 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]


def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


print(solution(s0))
print(solution(s1))
print(solution(s2))
