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

# 내가 푼 문제 풀이 방법 -> 정확성 테스트에서 시간초과로 걸림
from itertools import combinations
def solution(number, k):
    answer = 0
    cnt = list(combinations(range(len(number)), k))
    for i in cnt:
        tmp = ''
        for j in range(len(number)):
            if j not in i:
                tmp += number[j]
        answer = max(int(tmp), answer)
    return str(answer)

print(solution(n0, k0))
print(solution(n1, k1))
print(solution(n2, k2))
