from collections import defaultdict


def solution(n, results):
    answer = 0
    win_dic = defaultdict(set)
    lose_dic = defaultdict(set)

    for win, lose in results:
        lose_dic[lose].add(win)
        win_dic[win].add(lose)

    for i in range(1, n + 1):
        for win in win_dic[i]:
            lose_dic[win].update(lose_dic[i])
        for lose in lose_dic[i]:
            win_dic[lose].update(win_dic[i])

    for i in range(1, n + 1):
        if len(lose_dic[i]) + len(win_dic[i]) == n - 1:
            answer += 1

    return answer


res = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(5, res))
