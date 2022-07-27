def solution(s):
    answer = []
    stk = []
    for i in s:
        for j in range(len(i)):
            if i[j] == '0' and i[j-2:j-1] == '11':
                stk.append('110')
    print(stk)
    return answer


print(solution(["1110", "100111100", "0111111010"]))
