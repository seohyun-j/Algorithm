n0 = 1
n1 = 2
n2 = 3
n3 = 4


def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n // 3 - 1
    return answer[::-1]


for i in range(1, 11):
    print(solution(i))
