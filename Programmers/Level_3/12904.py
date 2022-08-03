def solution(s):
    answer = 1
    length = len(s)

    for i in range(length):
        for j in range(i + 2, length + 1):
            chk = s[i:j]

            if len(chk) > length:
                continue

            if chk == chk[::-1]:
                answer = max(answer, j - i)

                if answer == length:
                    return answer

    return answer


print(solution("abcdcba"))
print(solution("abacde"))
