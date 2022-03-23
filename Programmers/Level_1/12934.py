n0 = 121
n1 = 3

import math
def solution(n):
    k = int(math.sqrt(n))
    return pow(k+1,2) if pow(k,2)==n else -1

print(solution(n0))
print(solution(n1))