arr_p = ["(()())()", ")(", "()))((()"]


def divide(d):
    openP = 0
    closeP = 0

    for i in range(len(d)):
        if d[i] == '(':
            openP += 1
        else:
            closeP += 1
        if openP == closeP:
            return d[:i + 1], d[i + 1:]


def balanced(b):
    stack = []

    for i in b:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    if not p:
        return ""

    u, v = divide(p)

    if balanced(u):
        return u + solution(v)
    else:
        answer = '('
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
