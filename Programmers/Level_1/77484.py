l0 = [44, 1, 0, 0, 31, 25]
l1 = [0, 0, 0, 0, 0, 0]
l2 = [45, 4, 35, 20, 3, 9]
w0 = [31, 10, 45, 1, 6, 19]
w1 = [38, 19, 20, 40, 15, 25]
w2 = [20, 9, 3, 45, 4, 35]


def solution(lottos, win):
    verification = [6, 6, 5, 4, 3, 2, 1]
    key = 0
    for i in lottos:
      if i in win:
        key += 1
    good = key + lottos.count(0)
    return [verification[good], verification[key]]


print(solution(l0, w0))
print(solution(l1, w1))
print(solution(l2, w2))