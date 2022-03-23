n0 = 3
n1 = 2
m0 = 12
m1 = 5

import math
def solution(n, m):
    return [math.gcd(n, m), n*m//math.gcd(n, m)]

# 최대공약수 = math.gcd(숫자들)
# 최소공약수 = math.lcm(숫자들) or 숫자들 곱/최대공약수

print(solution(n0, m0))
print(solution(n1, m1))