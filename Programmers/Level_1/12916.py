s0 = "pPoooyY"
s1 = "Pyy"

def solution(s):
    s = s.lower()
    p, y = 0, 0
    for i in s:
      if i=='p':
        p += 1
      elif i=='y':
        y += 1
    return True if p==y else False

def second_solution(s):
    s = list(s.lower())
    return True if s.count('p') == s.count('y') else False

print(solution(s0))
print(solution(s1))