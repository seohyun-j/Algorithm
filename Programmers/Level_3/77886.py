def solution(s):
    answer = []
    for string in s:
        stack = []
        cnt = 0
        for st in string:
            if len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and st == '0':
                cnt += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(st)

        sub_cnt = 0
        for st in stack[::-1]:
            if st == '0':
                break
            else:
                sub_cnt += 1
        answer.append(''.join(stack[:len(stack) - sub_cnt]) + cnt * '110' + sub_cnt * '1')
    return answer


print(solution(["1110", "100111100", "0111111010"]))
