def solution(a, b, g, s, w, t):
    answer = 4 * (10 ** 14)
    high = 4 * (10 ** 14)
    low = 0

    while low <= high:
        mid = (low + high) // 2
        gold, sliver, total = 0, 0, 0

        for i in range(len(g)):
            ng, ns, nw, nt = g[i], s[i], w[i], t[i]

            move = mid // (nt * 2)

            if mid % (nt * 2) >= nt:
                move += 1

            gold += ng if move * nw > ng else move * nw
            sliver += ns if move * nw > ns else move * nw
            total += (ng + ns) if move * nw > (ns + ng) else move * nw

        if gold >= a and sliver >= b and total >= a + b:
            high = mid - 1
            answer = min(answer, mid)
        else:
            low = mid + 1

    return answer


print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
