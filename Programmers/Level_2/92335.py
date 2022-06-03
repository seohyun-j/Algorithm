n0, k0 = 437674, 3
n1, k1 = 110011, 10

import math


def convert(num, x):
    tmp = ''
    while num > 0:
        num, mod = divmod(num, x)
        tmp += str(mod)
    return tmp[::-1].split('0')


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    test = convert(n, k)
    for i in test:
        if i == '' or i == '1':
            continue
        if is_prime(int(i)):
            answer += 1
    return answer


print(solution(n0, k0))
print(solution(n1, k1))
