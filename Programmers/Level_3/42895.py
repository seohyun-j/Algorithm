def solution(N, number):
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i // 2 + 1):
            print(j, i-j)
            for first in dp[j]:
                for second in dp[i - j]:
                    dp[i] |= {first + second, first - second, second - first, first * second}

                    if first != 0:
                        dp[i].add(second // first)

                    if second != 0:
                        dp[i].add(first // second)
        print(dp[i])
        if number in dp[i]:
            return i

    return -1


print(solution(5, 12))
print(solution(2, 11))
print(solution(5, 31168))
