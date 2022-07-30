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


print(solution([0]))
print(solution([5, 2, 3, 3, 5, 3]))
print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
