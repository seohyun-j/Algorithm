s0 = ["Jane", "Kim"]

def solution(seoul):
  if "Kim" in seoul:
    return '김서방은 '+str(seoul.index("Kim"))+"에 있다"

print(solution(s0))