x0 = 2
x1 = 4
x2 = -4
n0 = 5
n1 = 3
n2 = 2

def solution(x, n):
    return [x*i for i in range(1,n+1)]

print(solution(x0, n0))
print(solution(x1, n1))
print(solution(x2, n2))