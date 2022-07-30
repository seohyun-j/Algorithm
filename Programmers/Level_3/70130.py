from itertools import combinations


def solution(a):
    length = len(a) if len(a) % 2 == 0 else len(a) - 1

    if length == 0:
        return 0

    for i in range(length, 1, -2):
        for arr in set(combinations(a, i)):
            chk = False
            before_set = [arr[0], arr[1]]

            for j in range(2, len(arr), 2):
                inter = set()
                next_set = [arr[j], arr[j + 1]]
                inter_set = set(before_set) & set(next_set)

                if not inter_set:
                    break

                if len(inter) == 0:
                    inter = inter_set
                else:
                    inter = inter & inter_set

                if len(set(before_set)) == 1:
                    chk = True

                before_set = next_set

            if not inter or chk:
                continue
            else:
                return len(arr)

    return 0


from collections import Counter


def other_solution(a):
    if len(a) < 4:
        return 0

    counter = Counter(a)
    answer = -1
    length = len(a) - 1

    for key in counter.keys():
        if counter[key] <= answer:
            continue

        i, cnt = 0, 0
        while i < length:
            if (a[i] == a[i + 1]) or (a[i] != key and a[i + 1] != key):
                i += 1
            else:
                i += 2
                cnt += 1
        answer = max(answer, cnt)

    return answer * 2


# https://yabmoons.tistory.com/610
print(solution([0]))
print(solution([5, 2, 3, 3, 5, 3]))
print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
print(other_solution([0]))
print(other_solution([5, 2, 3, 3, 5, 3]))
print(other_solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
