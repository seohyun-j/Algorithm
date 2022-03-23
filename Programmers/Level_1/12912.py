a0 = 3
b0 = 5
a1 = 3
b1 = 3
a2 = 5
b2 = 3

def solution(a,b):
  if a > b : a, b = b, a
  return sum(range(a,b+1))

print(solution(a0,b0))
print(solution(a1,b1))
print(solution(a2,b2))