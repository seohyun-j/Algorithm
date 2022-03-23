s0 = "AB"
s1 = "z"
s2 = "a B z"
n0 = 1
n1 = 1
n2 = 4

def solution(s, n):
    answer = ''
    for i in s:
      if i==' ':
        answer+=' '
      elif i.islower():
        answer+=chr((ord(i)-ord('a')+n)%26+ord('a'))
      else:
        answer+=chr((ord(i)-ord('A')+n)%26+ord('A'))
    return answer

print(solution(s0, n0))
print(solution(s1, n1))
print(solution(s2, n2))