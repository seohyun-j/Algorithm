n0 = 12
n1 = 5

def solution(n):
    answer = 0
    for i in range(1,n+1):
      if n%i == 0:
        answer+=i
    return answer

print(solution(n0))
print(solution(n1))