s0 = "a234"
s1 = "1234"

def solution(s):
    return True if (len(s)==4 or len(s)==6) and s.isdigit() else False

print(solution(s0))
print(solution(s1))