def solution(s):
    answer = []
    for i in s:
        while '110' in i:
            idx = i.index('110')
            i = '110' + i[:idx] + i[idx+4:]
            print(i)
            break
        answer.append(i)
    return s

print(solution(["1110","100111100","0111111010"]))