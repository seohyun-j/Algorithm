def solution(gems):
    answer = []
    short = len(gems) + 1
    st, en = 0, 0
    chk = len(set(gems))
    contain = {}

    while en < len(gems):
        if gems[en] not in contain:
            contain[gems[en]] = 1
        else:
            contain[gems[en]] += 1

        en += 1

        if len(contain) == chk:
            while st < en:
                if contain[gems[st]] > 1:
                    contain[gems[st]] -= 1
                    st += 1
                elif short > en - st:
                    short = en - st
                    answer = [st+1, en]
                    break
                else:
                    break

    return answer


g0 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
g1 = ["AA", "AB", "AC", "AA", "AC"]
g2 = ["XYZ", "XYZ", "XYZ"]
g3 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

print(solution(g0))
print(solution(g1))
print(solution(g2))
print(solution(g3))
