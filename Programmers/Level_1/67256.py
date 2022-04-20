n0 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
n1 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
n2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
h0 = "right"
h1 = "left"
h2 = "right"


def solution(numbers, hand):
    answer = ''
    key = [[1, 4, 7, '*'], [3, 6, 9, '#'], [2, 5, 8, 0]]
    Lqueue = ['*']
    Rqueue = ['#']
    for i in numbers:
        if i in key[0]:
            answer += 'L'
            Lqueue.append(i)

        elif i in key[1]:
            answer += 'R'
            Rqueue.append(i)

        elif i in key[2]:
            dis_l = abs(key[0].index(Lqueue[-1]) - key[2].index(i)) + 1 if Lqueue[-1] in key[0] else abs(
                key[2].index(Lqueue[-1]) - key[2].index(i))
            dis_r = abs(key[1].index(Rqueue[-1]) - key[2].index(i)) + 1 if Rqueue[-1] in key[1] else abs(
                key[2].index(Rqueue[-1]) - key[2].index(i))
            if dis_l > dis_r:
                answer += 'R'
                Rqueue.append(i)
            elif dis_l < dis_r:
                answer += 'L'
                Lqueue.append(i)
            elif dis_l == dis_r:
                if hand == "right":
                    answer += 'R'
                    Rqueue.append(i)
                else:
                    answer += 'L'
                    Lqueue.append(i)

    return answer


print(solution(n0, h0))
print(solution(n1, h1))
print(solution(n2, h2))
