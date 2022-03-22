w0 = 8
h0 = 12

import math
def solution(w, h):
    return w*h - (w+h - math.gcd(w, h))

print(solution(w0, h0))