s0 = "one4seveneight"
s1 = "23four5six7"
s2 = "2three45sixseven"
s3 = "123"


def solution(s):
    answer = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in answer:
        if i in s:
            s = s.replace(i, str(answer.index(i)))
    return int(s)


print(solution(s0))
print(solution(s1))
print(solution(s2))
