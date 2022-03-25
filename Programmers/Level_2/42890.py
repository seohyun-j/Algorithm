r = [["100", "ryan", "music", "2"],
     ["200", "apeach", "math", "2"],
     ["300", "tube", "computer", "3"],
     ["400", "con", "computer", "4"],
     ["500", "muzi", "music", "3"],
     ["600", "apeach", "music", "2"]]

from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    uni = []
    for i in combi:
        tmp = [tuple(item[key] for key in i) for item in relation]

        if len(set(tmp)) == row:
            put = True
            for x in uni:
                if set(x).issubset(set(i)):
                    put = False
                    break
            if put: uni.append(i)

    return len(uni)


print(solution(r))
