def solution(a):
    result = [False for _ in range(len(a))]
    min_left, min_right = float("inf"), float("inf")

    for i in range(len(a)):
        if a[i] < min_left:
            min_left = a[i]
            result[i] = True

        if a[-1 - i] < min_right:
            min_right = a[-1 - i]
            result[-1 - i] = True

        if min_left == min_right:
            break

    return sum(result)


a0 = [9, -1, -5]
a1 = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]

print(solution(a0))
print(solution(a1))
