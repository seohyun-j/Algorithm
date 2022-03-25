place = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
         ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
         ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
         ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
         ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

from itertools import combinations


def solution(places):
    answer = []

    for i in places:
        place_p = []
        for j in range(len(i)):
            for k in range(len(i[j])):
                if i[j][k] == "P":
                    place_p.append((j, k))
        place_p = list(combinations(place_p, 2))
        if place_p == []:
            answer.append(1)
        else:
            for p in place_p:
                x1, x2, y1, y2 = p[0][0], p[1][0], p[0][1], p[1][1]
                distance = abs(x1 - x2) + abs(y1 - y2)
                if distance < 2:
                    answer.append(0)
                    break
                elif distance == 2:
                    if x1 == x2 and i[x1][y1 + 1] == "O":
                        answer.append(0)
                        break
                    elif y1 == y2 and i[x1 + 1][y1] == "O":
                        answer.append(0)
                        break
                    elif i[x1][y2] == "O" or i[x2][y1] == "O":
                        answer.append(0)
                        break
                else:
                    pass

                if p == place_p[-1]:
                    answer.append(1)
    return answer


print(solution(place))