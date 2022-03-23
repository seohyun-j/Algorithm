n0 = 45
n1 = 125

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

print(solution(n0))
print(solution(n1))