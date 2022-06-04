s0 = "3people unFollowed me"
s1 = "for the last week"


def solution(s):
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    return ' '.join(s)


print(solution(s0))
print(solution(s1))
