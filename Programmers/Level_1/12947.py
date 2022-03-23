n0 = 10
n1 = 12
n2 = 13
n3 = 14

def solution(x):
    return x % sum([int(i) for i in str(x)]) == 0

print(solution(n0))
print(solution(n1))
print(solution(n2))
print(solution(n3))