n0 = "1924"
n1 = "1231234"
n2 = "4177252841"
k0 = 2
k1 = 3
k2 = 4

from itertools import combinations


def solution(number, k):
    answer = ''
    number = [i for i in number]
    num_arr = combinations(number, len(number) - k)

    return answer


print(solution(n0, k0))
print(solution(n1, k1))
print(solution(n2, k2))
