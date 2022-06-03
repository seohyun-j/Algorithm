n0, t0, m0, p0 = 2, 4, 2, 1
n1, t1, m1, p1 = 16, 16, 2, 1
n2, t2, m2, p2 = 16, 16, 2, 2


def convert(num, base):
    num_str = '0123456789ABCDEF'
    q, mod = divmod(num, base)

    if q == 0:
        return num_str[mod]
    else:
        return convert(q, base) + num_str[mod]


def solution(n, t, m, p):
    answer, tmp = '', ''

    for i in range(m * t):
        tmp += str(convert(i, n))

    print(tmp)

    while len(answer) < t:
        answer += tmp[p - 1]
        p += m

    return answer


print(solution(n0, t0, m0, p0))
print(solution(n1, t1, m1, p1))
print(solution(n2, t2, m2, p2))
