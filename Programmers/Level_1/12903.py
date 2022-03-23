s0 = "abcde"
s1 = "qwer"


def solution(s):
    return s[len(s) // 2] if len(s) % 2 == 1 else s[len(s) // 2 - 1:len(s) // 2 + 1]


print(solution(s0))
print(solution(s1))
