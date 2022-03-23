s0 = "try hello world"

def solution(s):
    answer = ''
    i = 0
    for k in s:
      if k==' ':
        i = 0
        answer += ' '
      else:
        if i%2==0:
          answer += k.upper()
        else:
          answer += k.lower()
        i += 1
    return answer

print(solution(s0))