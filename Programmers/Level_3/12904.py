def solution(s):
    answer = 0
    length = len(s)

    for i in range(length):
        for j in range(i + 2, length + 1):
            chk = s[i:j]
            if chk == chk[::-1]:
                answer = max(answer, j - i)

    return answer


print(solution("abcdcba"))
print(solution("abacde"))
