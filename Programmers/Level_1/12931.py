n0 = 123
n1 = 987

def solution(n):
    return sum([int(i) for i in str(n)])

print(solution(n0))
print(solution(n1))