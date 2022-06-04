def solution(n):
    fibo = [0, 1, 1]
    for i in range(3, n + 1):
        fibo.append(fibo[i - 2] + fibo[i - 1])
    return fibo[n] % 1234567


print(solution(3))
print(solution(5))
