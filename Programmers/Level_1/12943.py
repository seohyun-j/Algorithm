n0 = 6
n1 = 16
n2 = 626331

def solution(num):
    answer = 0
    while True:
      if num == 1:
        return answer
      elif answer>=500:
        return -1
      elif num%2 == 0:
        num = num // 2
      elif num%2 != 0:
        num = num * 3 + 1
      answer += 1

print(solution(n0))
print(solution(n1))
print(solution(n2))