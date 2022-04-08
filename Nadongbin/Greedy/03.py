import sys

N, K = map(int, sys.stdin.readline().split())
sum = 0  # 출력값 즉, 답
while N > 1:
    if N % K == 0:
        N = N / K
        sum += 1
    else:
        N -= 1
        sum += 1

print(sum)