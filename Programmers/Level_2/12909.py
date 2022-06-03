arr = ["()()", "(())()", ")()(", "(()("]


def solution(s):
    answer = 0

    for val in s:
        if val == ')' and answer == 0:
            return False

        if val == '(':
            answer += 1
        else:
            answer -= 1

    return True if answer == 0 else False


for i in arr:
    print(solution(i))
