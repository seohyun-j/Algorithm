ex0 = "...!@BaT#*..y.abcdefghijklm"
ex1 = "z-+.^."
ex2 = "=.="
ex3 = "123_.def"
ex4 = "abcdefghijklmn.p"


def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for i in new_id:
        if i.isalnum() or i in '._-':
            answer += i
    while '..' in answer:
        answer = answer.replace('..', '.')
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    answer = 'a' if len(answer) == 0 else answer
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer[:-1] if answer[-1] == '.' else answer
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
    return answer


print(solution(ex0))
print(solution(ex1))
print(solution(ex2))
print(solution(ex3))
print(solution(ex4))
