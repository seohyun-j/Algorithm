arr_p = ["(()())()", ")(", "()))((()"]


def check_bal(k):
    stack = []
    for i in k:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def check_count(k):
    left_word, right_word = 0, 0
    for idx, val in enumerate(k):
        if val == '(':
            left_word += 1
        else:
            right_word += 1
        if left_word == right_word:
            return k[:idx + 1], k[idx + 1:]


def solution(p):
    answer = ''

    # 과정 1
    if not p:
        return ''

    # 과정 2
    u, v = check_count(p)

    # 과정 3
    if check_bal(u):
        return u + solution(v)

    # 과정 4
    else:
        answer += '('
        answer += solution(v)
        answer += ')'

        for i in u[1:len(u) - 1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('

    return answer


for i in arr_p:
    print(solution(i))
