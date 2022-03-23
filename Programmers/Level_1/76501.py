a0 = [4, 7, 12]
a1 = [1, 2, 3]
s0 = [True, False, True]
s1 = [False, False, True]

def solution(absolutes, signs):
    answer = 0
    for p1, p2 in zip(absolutes, signs):
      if p2:
        answer += p1
      else:
        answer -= p1
    return answer

print(solution(a0, s0))
print(solution(a1, s1))