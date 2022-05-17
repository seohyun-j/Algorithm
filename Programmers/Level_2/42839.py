n0 = "17"
n1 = "011"

import math
def is_prime(x):
  if x==0 or x==1 :
    return False
  else:
    for i in range(2, int(math.sqrt(x))+1):
      if x%i == 0:
        return False
  return True

from itertools import permutations
def solution(numbers):
    answer = []
    numbers = [i for i in numbers]
    for i in range(1,len(numbers)+1):
      arr = list(permutations(numbers,i))
      for j in arr:
          num = int(''.join(map(str, j)))
          if num in answer:
              pass
          elif is_prime(num):
              answer.append(num)
    return len(answer)    

# 다른 사람 풀이 : 위의 풀이보다는 직관적이지만 느리다.
from itertools import permutations
def other_solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

print(solution(n0))
print(solution(n1))

print(other_solution(n0))
print(other_solution(n1))