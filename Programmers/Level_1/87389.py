n0 = 10
n1 = 12

def solution(n):
    for i in range(1,n+1):
      if n%i == 1:
        return i

print(solution(n0))
print(solution(n1))