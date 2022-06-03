n0, n1 = 78, 15


def solution(n):
    answer = n
    bin_n = bin(n)[2:]
    while True:
        answer += 1
        bin_a = bin(answer)[2:]
        if bin_n.count('1') == bin_a.count('1'):
            return answer


print(solution(n0))
print(solution(n1))
