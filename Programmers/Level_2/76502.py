s0 = "[](){}"
s1 = "}]()[{"
s2 = "[)(]"
s3 = "}}}"

from collections import deque

def check(x):
    stack = []
    for c in x:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if not stack:
                return False
            x = stack.pop()
            if c == ')' and x != '(':
                return False
            elif c == '}' and x != '{':
                return False
            elif c == ']' and x != '[':
                return False
    return len(stack) == 0

def dic_check(x):
    dic = {'(':0, '[':0, '{':0}
    for i in x:
        if i in ['{', '(', '[']:
            dic[i] += 1
        else:
            if i == ')' and dic['('] > 0:
                dic['('] -= 1
            elif i == ']' and dic['['] > 0:
                dic['['] -= 1
            elif i == '}' and dic['{'] > 0:
                dic['{'] -= 1
            else:
                return False
    return sum(dic.values()) == 0

def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        s.rotate(-1)
        if check(s):
            answer += 1
    return answer


print(solution(s0))
print(solution(s1))
print(solution(s2))
print(solution(s3))
