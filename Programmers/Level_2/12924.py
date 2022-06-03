def solution(n):
    answer = 0
    for i in range(1, n + 1):
        sum = 0
        for j in range(i, n + 1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
    return answer


# 수학적 접근
'''
    a + (a + 1) + (a + 2) + ... + (a + k - 1) = k * (2a + k - 1) / 2 = n
    이때, a와 k는 자연수이고, a <= n, k < n임
    n = k * (2a + k - 1) / 2를 a로 정리하면, a = n/k + (1 - k)/2임
    a가 자연수이려면 n/k와 (1 - k)/2가 정수여야함
    따라서, (1 - k)가 짝수이려면 k는 홀수이고, k는 n의 약수여야함
'''


def other_solution(n):
    return len([i for i in range(1, n + 1, 2) if n % i == 0])


print(solution(15))
print(other_solution(15))
